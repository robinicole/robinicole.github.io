"""
State tracking for Hugo-Obsidian sync.
Tracks file hashes to detect changes since last sync.
"""

import hashlib
import json
import os
from pathlib import Path
from typing import Dict, Optional


def get_state_path(config_state_file: str) -> Path:
    """Expand ~ and return Path object for state file."""
    return Path(os.path.expanduser(config_state_file))


def load_state(state_path: Path) -> Dict:
    """Load sync state from JSON file."""
    if not state_path.exists():
        return {"hugo": {}, "obsidian": {}, "format": {}}

    with open(state_path, "r") as f:
        state = json.load(f)
        # Ensure format key exists for backwards compatibility
        if "format" not in state:
            state["format"] = {}
        return state


def save_state(state_path: Path, state: Dict) -> None:
    """Save sync state to JSON file."""
    state_path.parent.mkdir(parents=True, exist_ok=True)
    with open(state_path, "w") as f:
        json.dump(state, f, indent=2)


def get_file_hash(file_path: Path) -> str:
    """Calculate MD5 hash of file contents."""
    if not file_path.exists():
        return ""

    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def get_file_mtime(file_path: Path) -> float:
    """Get file modification time."""
    if not file_path.exists():
        return 0.0
    return file_path.stat().st_mtime


def file_changed(file_path: Path, stored_hash: Optional[str]) -> bool:
    """Check if file has changed since last sync."""
    if stored_hash is None:
        return True
    return get_file_hash(file_path) != stored_hash
