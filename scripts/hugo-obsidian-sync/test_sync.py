#!/usr/bin/env python3
"""
Tests for Hugo-Obsidian sync tool.
"""

import shutil
import tempfile
from pathlib import Path

from converters import hugo_to_obsidian, obsidian_to_hugo
from state import load_state, save_state, get_file_hash
from sync import (
    get_post_id,
    scan_posts,
    sync_post_to_obsidian,
    sync_post_to_hugo,
)


class TestConverters:
    """Test shortcode conversion."""

    def test_mermaid_hugo_to_obsidian(self):
        hugo = """{{< mermaid >}}
graph LR
    A --> B
{{< /mermaid >}}"""
        expected = """```mermaid
graph LR
    A --> B
```"""
        assert hugo_to_obsidian(hugo) == expected

    def test_mermaid_obsidian_to_hugo(self):
        obsidian = """```mermaid
graph LR
    A --> B
```"""
        expected = """{{< mermaid >}}
graph LR
    A --> B
{{< /mermaid >}}"""
        assert obsidian_to_hugo(obsidian) == expected

    def test_mermaid_roundtrip(self):
        hugo = """{{< mermaid >}}
graph LR
    A --> B
{{< /mermaid >}}"""
        roundtrip = obsidian_to_hugo(hugo_to_obsidian(hugo))
        assert roundtrip == hugo

    def test_alert_hugo_to_obsidian(self):
        hugo = """{{< alert >}}
**Info:** test message
{{< /alert >}}"""
        result = hugo_to_obsidian(hugo)
        assert "> [!info]" in result
        assert "**Info:** test message" in result

    def test_ref_hugo_to_obsidian(self):
        hugo = '[here]({{< ref "intro-to-prompt-engineering.md" >}})'
        expected = "[[intro-to-prompt-engineering|here]]"
        assert hugo_to_obsidian(hugo) == expected

    def test_wikilink_obsidian_to_hugo(self):
        obsidian = "[[intro-to-prompt-engineering|here]]"
        expected = '[here]({{< ref "intro-to-prompt-engineering.md" >}})'
        assert obsidian_to_hugo(obsidian) == expected

    def test_ref_roundtrip(self):
        hugo = '[here]({{< ref "intro-to-prompt-engineering.md" >}})'
        roundtrip = obsidian_to_hugo(hugo_to_obsidian(hugo))
        assert roundtrip == hugo


class TestPostFormat:
    """Test that post format is preserved during sync."""

    def setup_method(self):
        """Create temp directories for each test."""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.hugo_dir = self.temp_dir / "hugo" / "content" / "posts"
        self.obsidian_dir = self.temp_dir / "obsidian" / "posts"
        self.hugo_dir.mkdir(parents=True)
        self.obsidian_dir.mkdir(parents=True)

    def teardown_method(self):
        """Clean up temp directories."""
        shutil.rmtree(self.temp_dir)

    def test_single_file_post_preserved(self):
        """Single-file posts should remain single files after round-trip."""
        # Create a single-file Hugo post
        hugo_post = self.hugo_dir / "my-post.md"
        hugo_post.write_text("""---
title: "My Post"
---
Content here.""")

        state = {"hugo": {}, "obsidian": {}, "format": {}}

        # Sync to Obsidian
        post_id = "my-post"
        sync_post_to_obsidian(hugo_post, self.obsidian_dir, post_id, state)

        # Verify format was recorded as single
        assert state["format"][post_id] == "single"

        # Verify Obsidian file was created correctly
        obsidian_post = self.obsidian_dir / "my-post.md"
        assert obsidian_post.exists()

        # Sync back to Hugo
        sync_post_to_hugo(obsidian_post, self.hugo_dir, post_id, state)

        # Verify it's still a single file (not a directory)
        assert hugo_post.exists()
        assert hugo_post.is_file()
        assert not (self.hugo_dir / "my-post" / "index.md").exists()

    def test_directory_post_preserved(self):
        """Directory-style posts should remain directories after round-trip."""
        # Create a directory-style Hugo post
        hugo_post_dir = self.hugo_dir / "my-gallery"
        hugo_post_dir.mkdir()
        hugo_post = hugo_post_dir / "index.md"
        hugo_post.write_text("""---
title: "My Gallery"
---
Content with images.""")

        # Add an image
        (hugo_post_dir / "photo.png").write_bytes(b"fake png data")

        state = {"hugo": {}, "obsidian": {}, "format": {}}

        # Sync to Obsidian
        post_id = "my-gallery"
        sync_post_to_obsidian(hugo_post, self.obsidian_dir, post_id, state)

        # Verify format was recorded as directory
        assert state["format"][post_id] == "directory"

        # Verify Obsidian files were created correctly
        obsidian_post_dir = self.obsidian_dir / "my-gallery"
        obsidian_post = obsidian_post_dir / "my-gallery.md"
        assert obsidian_post.exists()
        assert (obsidian_post_dir / "photo.png").exists()

        # Sync back to Hugo
        sync_post_to_hugo(obsidian_post, self.hugo_dir, post_id, state)

        # Verify it's still a directory with index.md (not my-gallery.md)
        assert hugo_post.exists()  # index.md
        assert hugo_post.is_file()
        assert not (self.hugo_dir / "my-gallery.md").exists()

    def test_no_nested_directories_on_roundtrip(self):
        """Syncing back should not create nested directories."""
        # Create a directory-style Hugo post
        hugo_post_dir = self.hugo_dir / "obsidian_and_note_taking"
        hugo_post_dir.mkdir()
        hugo_post = hugo_post_dir / "index.md"
        hugo_post.write_text("""---
title: "Notes on Note Taking"
---
{{< mermaid >}}
graph LR
    A --> B
{{< /mermaid >}}""")

        # Add an image
        (hugo_post_dir / "featured.jpeg").write_bytes(b"fake jpeg data")

        state = {"hugo": {}, "obsidian": {}, "format": {}}
        post_id = "obsidian_and_note_taking"

        # Sync Hugo -> Obsidian
        sync_post_to_obsidian(hugo_post, self.obsidian_dir, post_id, state)

        obsidian_post = self.obsidian_dir / post_id / f"{post_id}.md"
        assert obsidian_post.exists()

        # Sync Obsidian -> Hugo
        sync_post_to_hugo(obsidian_post, self.hugo_dir, post_id, state)

        # THE KEY TEST: No nested directory should exist
        nested_path = self.hugo_dir / post_id / post_id / "index.md"
        assert not nested_path.exists(), f"Nested directory created: {nested_path}"

        # Original structure should be preserved
        assert (self.hugo_dir / post_id / "index.md").exists()


class TestState:
    """Test state tracking."""

    def setup_method(self):
        self.temp_dir = Path(tempfile.mkdtemp())
        self.state_path = self.temp_dir / "state.json"

    def teardown_method(self):
        shutil.rmtree(self.temp_dir)

    def test_load_empty_state(self):
        state = load_state(self.state_path)
        assert state == {"hugo": {}, "obsidian": {}, "format": {}}

    def test_save_and_load_state(self):
        state = {
            "hugo": {"post1": "hash1"},
            "obsidian": {"post1": "hash2"},
            "format": {"post1": "single"},
        }
        save_state(self.state_path, state)
        loaded = load_state(self.state_path)
        assert loaded == state

    def test_backwards_compatibility(self):
        """Old state files without format key should work."""
        import json
        old_state = {"hugo": {}, "obsidian": {}}
        with open(self.state_path, "w") as f:
            json.dump(old_state, f)

        loaded = load_state(self.state_path)
        assert "format" in loaded


class TestPostId:
    """Test post ID generation."""

    def setup_method(self):
        self.temp_dir = Path(tempfile.mkdtemp())

    def teardown_method(self):
        shutil.rmtree(self.temp_dir)

    def test_single_file_post_id(self):
        post = self.temp_dir / "my-post.md"
        post.touch()
        assert get_post_id(post, self.temp_dir) == "my-post"

    def test_directory_post_id(self):
        post_dir = self.temp_dir / "my-gallery"
        post_dir.mkdir()
        post = post_dir / "index.md"
        post.touch()
        assert get_post_id(post, self.temp_dir) == "my-gallery"


def run_tests():
    """Run all tests and report results."""
    import traceback

    test_classes = [TestConverters, TestPostFormat, TestState, TestPostId]
    passed = 0
    failed = 0

    for test_class in test_classes:
        print(f"\n{test_class.__name__}")
        print("-" * 40)

        instance = test_class()
        for method_name in dir(instance):
            if method_name.startswith("test_"):
                # Setup
                if hasattr(instance, "setup_method"):
                    instance.setup_method()

                try:
                    getattr(instance, method_name)()
                    print(f"  ✓ {method_name}")
                    passed += 1
                except AssertionError as e:
                    print(f"  ✗ {method_name}: {e}")
                    failed += 1
                except Exception as e:
                    print(f"  ✗ {method_name}: {e}")
                    traceback.print_exc()
                    failed += 1
                finally:
                    # Teardown
                    if hasattr(instance, "teardown_method"):
                        instance.teardown_method()

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")
    return failed == 0


if __name__ == "__main__":
    import sys
    success = run_tests()
    sys.exit(0 if success else 1)
