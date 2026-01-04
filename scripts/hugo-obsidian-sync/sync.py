#!/usr/bin/env python3
"""
Hugo-Obsidian Bidirectional Sync Tool

Syncs markdown posts between a Hugo blog and an Obsidian vault,
converting shortcodes between formats.

Usage:
    python sync.py              # Bidirectional sync
    python sync.py --push       # Obsidian -> Hugo only
    python sync.py --pull       # Hugo -> Obsidian only
    python sync.py --dry-run    # Show what would change
    python sync.py --force hugo # Hugo wins all conflicts
"""

import argparse
import difflib
import os
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

from converters import hugo_to_obsidian, obsidian_to_hugo
from state import (
    file_changed,
    get_file_hash,
    get_file_mtime,
    get_state_path,
    load_state,
    save_state,
)


class SyncAction:
    """Represents a sync action to be taken."""
    NEW_IN_OBSIDIAN = "new_in_obsidian"
    NEW_IN_HUGO = "new_in_hugo"
    MODIFIED_IN_OBSIDIAN = "modified_in_obsidian"
    MODIFIED_IN_HUGO = "modified_in_hugo"
    CONFLICT = "conflict"
    UNCHANGED = "unchanged"
    DELETED_IN_OBSIDIAN = "deleted_in_obsidian"
    DELETED_IN_HUGO = "deleted_in_hugo"


def load_config(config_path: Path) -> Dict:
    """Load configuration from YAML file."""
    if not config_path.exists():
        print(f"Error: Config file not found: {config_path}")
        print("Please create a config.yaml file. See config.yaml.example for template.")
        sys.exit(1)

    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def get_post_id(path: Path, base_dir: Path) -> str:
    """Get a unique identifier for a post based on its path."""
    rel_path = path.relative_to(base_dir)

    # For directory-style posts (index.md), use the directory name
    if path.name == "index.md":
        return str(rel_path.parent)

    # For single-file posts, use the filename without extension
    return str(rel_path.with_suffix(""))


def scan_posts(directory: Path) -> Dict[str, Path]:
    """Scan a directory for markdown posts and return {post_id: path}."""
    posts = {}

    if not directory.exists():
        return posts

    for md_file in directory.rglob("*.md"):
        # Skip non-post files
        if md_file.name.startswith("_"):
            continue

        post_id = get_post_id(md_file, directory)
        posts[post_id] = md_file

    return posts


def determine_action(
    post_id: str,
    hugo_path: Optional[Path],
    obsidian_path: Optional[Path],
    state: Dict,
) -> Tuple[str, Optional[str]]:
    """Determine what sync action to take for a post.

    Returns (action, detail) tuple.
    """
    hugo_hash = state.get("hugo", {}).get(post_id)
    obsidian_hash = state.get("obsidian", {}).get(post_id)

    hugo_exists = hugo_path is not None and hugo_path.exists()
    obsidian_exists = obsidian_path is not None and obsidian_path.exists()

    # Handle new files
    if hugo_exists and not obsidian_exists and not obsidian_hash:
        return SyncAction.NEW_IN_HUGO, None
    if obsidian_exists and not hugo_exists and not hugo_hash:
        return SyncAction.NEW_IN_OBSIDIAN, None

    # Handle deletions
    if not hugo_exists and obsidian_exists and hugo_hash:
        return SyncAction.DELETED_IN_HUGO, None
    if not obsidian_exists and hugo_exists and obsidian_hash:
        return SyncAction.DELETED_IN_OBSIDIAN, None

    # Both exist - check for modifications
    if hugo_exists and obsidian_exists:
        hugo_changed = file_changed(hugo_path, hugo_hash)
        obsidian_changed = file_changed(obsidian_path, obsidian_hash)

        if hugo_changed and obsidian_changed:
            return SyncAction.CONFLICT, "Both sides modified"
        elif hugo_changed:
            return SyncAction.MODIFIED_IN_HUGO, None
        elif obsidian_changed:
            return SyncAction.MODIFIED_IN_OBSIDIAN, None

    return SyncAction.UNCHANGED, None


def show_diff(hugo_content: str, obsidian_content: str) -> None:
    """Display a diff between Hugo and Obsidian versions."""
    hugo_lines = hugo_content.splitlines(keepends=True)
    obsidian_lines = obsidian_content.splitlines(keepends=True)

    diff = difflib.unified_diff(
        hugo_lines,
        obsidian_lines,
        fromfile="Hugo",
        tofile="Obsidian",
        lineterm=""
    )

    print("\n--- Diff (Hugo vs Obsidian) ---")
    for line in diff:
        if line.startswith("+"):
            print(f"\033[92m{line}\033[0m", end="")
        elif line.startswith("-"):
            print(f"\033[91m{line}\033[0m", end="")
        else:
            print(line, end="")
    print("\n--- End Diff ---\n")


def resolve_conflict(
    post_id: str,
    hugo_path: Path,
    obsidian_path: Path,
    force: Optional[str] = None,
) -> Optional[str]:
    """Resolve a conflict between Hugo and Obsidian versions.

    Returns 'hugo', 'obsidian', or None to skip.
    """
    if force:
        return force

    hugo_content = hugo_path.read_text()
    obsidian_content = obsidian_path.read_text()

    print(f"\n{'='*60}")
    print(f"CONFLICT: {post_id}")
    print(f"Hugo:     {hugo_path}")
    print(f"Obsidian: {obsidian_path}")

    show_diff(hugo_content, obsidian_content)

    while True:
        choice = input("Keep [H]ugo / [O]bsidian / [S]kip? ").strip().lower()
        if choice in ("h", "hugo"):
            return "hugo"
        elif choice in ("o", "obsidian"):
            return "obsidian"
        elif choice in ("s", "skip"):
            return None
        print("Invalid choice. Enter H, O, or S.")


def sync_post_to_obsidian(
    hugo_path: Path,
    obsidian_dir: Path,
    post_id: str,
    state: Dict,
    dry_run: bool = False,
) -> Optional[Path]:
    """Sync a post from Hugo to Obsidian."""
    # Determine target path and record format
    if hugo_path.name == "index.md":
        # Directory-style post
        target_dir = obsidian_dir / post_id
        target_path = target_dir / f"{post_id.split('/')[-1]}.md"
        if not dry_run:
            state.setdefault("format", {})[post_id] = "directory"
    else:
        # Single-file post
        target_path = obsidian_dir / f"{post_id}.md"
        target_dir = target_path.parent
        if not dry_run:
            state.setdefault("format", {})[post_id] = "single"

    if dry_run:
        print(f"  Would create: {target_path}")
        return target_path

    # Create directory if needed
    target_dir.mkdir(parents=True, exist_ok=True)

    # Convert and write content
    hugo_content = hugo_path.read_text()
    obsidian_content = hugo_to_obsidian(hugo_content)
    target_path.write_text(obsidian_content)

    # Copy assets for directory-style posts
    if hugo_path.name == "index.md":
        for asset in hugo_path.parent.iterdir():
            if asset.is_file() and asset.name != "index.md":
                dest = target_dir / asset.name
                shutil.copy2(asset, dest)

    return target_path


def sync_post_to_hugo(
    obsidian_path: Path,
    hugo_dir: Path,
    post_id: str,
    state: Dict,
    dry_run: bool = False,
) -> Optional[Path]:
    """Sync a post from Obsidian to Hugo."""
    # Use stored format from state, or detect from existing Hugo structure
    stored_format = state.get("format", {}).get(post_id)

    if stored_format == "directory":
        is_directory_style = True
    elif stored_format == "single":
        is_directory_style = False
    else:
        # Fallback: check if Hugo already has this as a directory
        existing_dir = hugo_dir / post_id
        existing_index = existing_dir / "index.md"
        existing_single = hugo_dir / f"{post_id}.md"

        if existing_index.exists():
            is_directory_style = True
        elif existing_single.exists():
            is_directory_style = False
        else:
            # New post - check if Obsidian has assets
            is_directory_style = False
            for sibling in obsidian_path.parent.iterdir():
                if sibling.is_file() and sibling.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif", ".svg"):
                    is_directory_style = True
                    break

    if is_directory_style:
        # Directory-style post
        target_dir = hugo_dir / post_id
        target_path = target_dir / "index.md"
    else:
        # Single-file post
        target_path = hugo_dir / f"{post_id}.md"
        target_dir = target_path.parent

    if dry_run:
        print(f"  Would create: {target_path}")
        return target_path

    # Create directory if needed
    target_dir.mkdir(parents=True, exist_ok=True)

    # Convert and write content
    obsidian_content = obsidian_path.read_text()
    hugo_content = obsidian_to_hugo(obsidian_content)
    target_path.write_text(hugo_content)

    # Copy assets if directory-style
    if is_directory_style:
        for asset in obsidian_path.parent.iterdir():
            if asset.is_file() and asset != obsidian_path:
                dest = target_dir / asset.name
                shutil.copy2(asset, dest)

    return target_path


def main():
    parser = argparse.ArgumentParser(
        description="Bidirectional sync between Hugo and Obsidian"
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Only sync Obsidian -> Hugo",
    )
    parser.add_argument(
        "--pull",
        action="store_true",
        help="Only sync Hugo -> Obsidian",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without making changes",
    )
    parser.add_argument(
        "--force",
        choices=["hugo", "obsidian"],
        help="Force one side to win all conflicts",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).parent / "config.yaml",
        help="Path to config file",
    )

    args = parser.parse_args()

    # Validate args
    if args.push and args.pull:
        print("Error: Cannot use --push and --pull together")
        sys.exit(1)

    # Load config
    config = load_config(args.config)
    hugo_dir = Path(os.path.expanduser(config["hugo_content"]))
    obsidian_dir = Path(os.path.expanduser(config["obsidian_vault"]))
    state_path = get_state_path(config.get("state_file", "~/.config/hugo-obsidian-sync/state.json"))

    # Validate directories
    if not hugo_dir.exists():
        print(f"Error: Hugo content directory not found: {hugo_dir}")
        sys.exit(1)

    if not obsidian_dir.exists():
        print(f"Creating Obsidian vault directory: {obsidian_dir}")
        if not args.dry_run:
            obsidian_dir.mkdir(parents=True, exist_ok=True)

    # Load state
    state = load_state(state_path)

    # Scan both directories
    hugo_posts = scan_posts(hugo_dir)
    obsidian_posts = scan_posts(obsidian_dir)

    # Get all post IDs
    all_post_ids = set(hugo_posts.keys()) | set(obsidian_posts.keys())

    print(f"Found {len(hugo_posts)} Hugo posts, {len(obsidian_posts)} Obsidian posts")
    print(f"Mode: {'dry-run' if args.dry_run else 'live'}")
    if args.push:
        print("Direction: Obsidian -> Hugo only")
    elif args.pull:
        print("Direction: Hugo -> Obsidian only")
    else:
        print("Direction: Bidirectional")
    print()

    # Process each post
    synced = 0
    skipped = 0
    conflicts = 0

    for post_id in sorted(all_post_ids):
        hugo_path = hugo_posts.get(post_id)
        obsidian_path = obsidian_posts.get(post_id)

        action, detail = determine_action(post_id, hugo_path, obsidian_path, state)

        if action == SyncAction.UNCHANGED:
            continue

        print(f"[{action}] {post_id}")

        # Handle based on action and mode
        if action == SyncAction.NEW_IN_HUGO:
            if not args.push:  # Pull or bidirectional
                sync_post_to_obsidian(hugo_path, obsidian_dir, post_id, state, args.dry_run)
                synced += 1
            else:
                skipped += 1

        elif action == SyncAction.NEW_IN_OBSIDIAN:
            if not args.pull:  # Push or bidirectional
                sync_post_to_hugo(obsidian_path, hugo_dir, post_id, state, args.dry_run)
                synced += 1
            else:
                skipped += 1

        elif action == SyncAction.MODIFIED_IN_HUGO:
            if not args.push:
                sync_post_to_obsidian(hugo_path, obsidian_dir, post_id, state, args.dry_run)
                synced += 1
            else:
                skipped += 1

        elif action == SyncAction.MODIFIED_IN_OBSIDIAN:
            if not args.pull:
                sync_post_to_hugo(obsidian_path, hugo_dir, post_id, state, args.dry_run)
                synced += 1
            else:
                skipped += 1

        elif action == SyncAction.CONFLICT:
            conflicts += 1
            if args.dry_run:
                print(f"  Conflict detected - would prompt for resolution")
                continue

            resolution = resolve_conflict(post_id, hugo_path, obsidian_path, args.force)
            if resolution == "hugo":
                sync_post_to_obsidian(hugo_path, obsidian_dir, post_id, state, args.dry_run)
                synced += 1
            elif resolution == "obsidian":
                sync_post_to_hugo(obsidian_path, hugo_dir, post_id, state, args.dry_run)
                synced += 1
            else:
                skipped += 1

        elif action in (SyncAction.DELETED_IN_HUGO, SyncAction.DELETED_IN_OBSIDIAN):
            print(f"  Deletion detected - skipping (manual review recommended)")
            skipped += 1

    # Update state (unless dry-run)
    if not args.dry_run:
        # Rescan and update hashes
        hugo_posts = scan_posts(hugo_dir)
        obsidian_posts = scan_posts(obsidian_dir)

        state["hugo"] = {pid: get_file_hash(path) for pid, path in hugo_posts.items()}
        state["obsidian"] = {pid: get_file_hash(path) for pid, path in obsidian_posts.items()}

        save_state(state_path, state)

    # Summary
    print()
    print(f"Summary: {synced} synced, {skipped} skipped, {conflicts} conflicts")


if __name__ == "__main__":
    main()
