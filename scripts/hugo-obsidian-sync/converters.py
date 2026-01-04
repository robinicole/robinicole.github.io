"""
Bidirectional converters between Hugo and Obsidian markdown formats.
"""

import re
from typing import Tuple


def hugo_to_obsidian(content: str) -> str:
    """Convert Hugo markdown to Obsidian format."""
    result = content

    # Convert mermaid shortcode to code block
    # {{< mermaid >}}...{{< /mermaid >}} -> ```mermaid...```
    result = re.sub(
        r'\{\{<\s*mermaid\s*>\}\}\n?(.*?)\n?\{\{<\s*/mermaid\s*>\}\}',
        r'```mermaid\n\1\n```',
        result,
        flags=re.DOTALL
    )

    # Convert alert shortcode to Obsidian callout
    # {{< alert >}}...{{< /alert >}} -> > [!info]...
    def convert_alert(match):
        alert_content = match.group(1).strip()
        # Indent each line with > for callout
        lines = alert_content.split('\n')
        callout_lines = ['> [!info]'] + ['> ' + line for line in lines]
        return '\n'.join(callout_lines)

    result = re.sub(
        r'\{\{<\s*alert\s*>\}\}\n?(.*?)\n?\{\{<\s*/alert\s*>\}\}',
        convert_alert,
        result,
        flags=re.DOTALL
    )

    # Convert ref shortcode to wikilink
    # [text]({{< ref "post.md" >}}) -> [[post|text]]
    def convert_ref(match):
        text = match.group(1)
        ref_path = match.group(2)
        # Remove .md extension and path components
        note_name = ref_path.replace('.md', '').split('/')[-1]
        if text == note_name:
            return f'[[{note_name}]]'
        return f'[[{note_name}|{text}]]'

    result = re.sub(
        r'\[([^\]]+)\]\(\{\{<\s*ref\s+"([^"]+)"\s*>\}\}\)',
        convert_ref,
        result
    )

    # Convert standard markdown images to Obsidian embed
    # ![alt](image.png) -> ![[image.png]]
    # Only for local images (not URLs)
    def convert_image(match):
        alt = match.group(1)
        path = match.group(2)
        # Skip URLs
        if path.startswith('http://') or path.startswith('https://'):
            return match.group(0)
        # Get just the filename
        filename = path.split('/')[-1]
        return f'![[{filename}]]'

    result = re.sub(
        r'!\[([^\]]*)\]\(([^)]+)\)',
        convert_image,
        result
    )

    return result


def obsidian_to_hugo(content: str) -> str:
    """Convert Obsidian markdown to Hugo format."""
    result = content

    # Convert mermaid code block to shortcode
    # ```mermaid...``` -> {{< mermaid >}}...{{< /mermaid >}}
    result = re.sub(
        r'```mermaid\n(.*?)\n```',
        r'{{< mermaid >}}\n\1\n{{< /mermaid >}}',
        result,
        flags=re.DOTALL
    )

    # Convert Obsidian callout to alert shortcode
    # > [!info]... -> {{< alert >}}...{{< /alert >}}
    def convert_callout(match):
        # Get all the callout lines
        callout_block = match.group(0)
        lines = callout_block.split('\n')

        # Extract content (remove > prefix and [!type] header)
        content_lines = []
        for i, line in enumerate(lines):
            if i == 0:
                # First line: > [!info] or > [!type] possibly with text after
                after_type = re.sub(r'^>\s*\[!(\w+)\]\s*', '', line)
                if after_type.strip():
                    content_lines.append(after_type)
            else:
                # Subsequent lines: remove > prefix
                content_lines.append(re.sub(r'^>\s?', '', line))

        content = '\n'.join(content_lines).strip()
        return f'{{{{< alert >}}}}\n{content}\n{{{{< /alert >}}}}'

    # Match callout blocks (lines starting with > [!type] followed by > lines)
    result = re.sub(
        r'^>\s*\[!(\w+)\].*(?:\n>.*)*',
        convert_callout,
        result,
        flags=re.MULTILINE
    )

    # Convert wikilink to ref shortcode
    # [[note|text]] -> [text]({{< ref "note.md" >}})
    # [[note]] -> [note]({{< ref "note.md" >}})
    def convert_wikilink(match):
        full_match = match.group(1)
        if '|' in full_match:
            note, text = full_match.split('|', 1)
        else:
            note = text = full_match

        # Add .md extension if not present
        if not note.endswith('.md'):
            note = note + '.md'

        return f'[{text}]({{{{< ref "{note}" >}}}})'

    result = re.sub(
        r'\[\[([^\]]+)\]\]',
        convert_wikilink,
        result
    )

    # Convert Obsidian image embed to standard markdown
    # ![[image.png]] -> ![](image.png)
    def convert_embed(match):
        filename = match.group(1)
        # Skip if it looks like a note link (no extension or .md)
        if '.' not in filename or filename.endswith('.md'):
            return match.group(0)
        return f'![]({filename})'

    result = re.sub(
        r'!\[\[([^\]]+)\]\]',
        convert_embed,
        result
    )

    return result


def detect_format(content: str) -> str:
    """Detect if content is in Hugo or Obsidian format.

    Returns 'hugo', 'obsidian', or 'unknown'.
    """
    hugo_patterns = [
        r'\{\{<\s*mermaid\s*>\}\}',
        r'\{\{<\s*alert\s*>\}\}',
        r'\{\{<\s*ref\s+"',
    ]

    obsidian_patterns = [
        r'```mermaid',
        r'^>\s*\[!\w+\]',
        r'\[\[[^\]]+\]\]',
        r'!\[\[[^\]]+\]\]',
    ]

    hugo_score = sum(1 for p in hugo_patterns if re.search(p, content))
    obsidian_score = sum(1 for p in obsidian_patterns if re.search(p, content, re.MULTILINE))

    if hugo_score > obsidian_score:
        return 'hugo'
    elif obsidian_score > hugo_score:
        return 'obsidian'
    return 'unknown'
