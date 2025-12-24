#!/usr/bin/env python3
"""
Rename MiniMax-generated audio files to match standard naming convention.

Usage:
    python rename_audio.py <directory> <story_name> <chapter_number>

Example:
    python rename_audio.py "重写时间的源代码/chapters" "重写时间的源代码" "01"

This will find the most recent MP3 file that doesn't match the expected pattern
and rename it to: 重写时间的源代码-01.mp3
"""

import os
import sys
import re
from pathlib import Path


def find_latest_non_standard_mp3(directory: str, story_name: str, chapter_num: str) -> Path | None:
    """Find the most recent MP3 that doesn't match the standard naming pattern."""
    dir_path = Path(directory)
    if not dir_path.exists():
        return None

    expected_pattern = f"{story_name}-{chapter_num}.mp3"

    # Get all MP3 files sorted by modification time (newest first)
    mp3_files = sorted(
        dir_path.glob("*.mp3"),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    for mp3_file in mp3_files:
        # Skip files that already match the expected pattern
        if mp3_file.name == expected_pattern:
            continue

        # Look for MiniMax-style filenames: t2a_*_YYYYMMDD_HHMMSS.mp3
        if mp3_file.name.startswith("t2a_") or re.match(r".+_\d{8}_\d{6}\.mp3$", mp3_file.name):
            return mp3_file

    return None


def rename_audio(directory: str, story_name: str, chapter_num: str) -> str:
    """
    Rename the latest non-standard MP3 to the standard format.

    Returns the new file path if successful, or an error message.
    """
    source_file = find_latest_non_standard_mp3(directory, story_name, chapter_num)

    if source_file is None:
        # Check if the expected file already exists
        expected_path = Path(directory) / f"{story_name}-{chapter_num}.mp3"
        if expected_path.exists():
            return f"File already exists: {expected_path}"
        return f"No non-standard MP3 found in {directory}"

    target_name = f"{story_name}-{chapter_num}.mp3"
    target_path = source_file.parent / target_name

    # Handle case where target already exists
    if target_path.exists():
        return f"Target already exists: {target_path}"

    source_file.rename(target_path)
    return f"Renamed: {source_file.name} -> {target_name}"


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)

    directory = sys.argv[1]
    story_name = sys.argv[2]
    chapter_num = sys.argv[3]

    result = rename_audio(directory, story_name, chapter_num)
    print(result)


if __name__ == "__main__":
    main()
