"""Module containing helper functions for Advent of Code puzzles."""

from collections.abc import Iterator

def read_file_lines(file) -> Iterator[str]:
    """Opens a given file and yields each line as needed.
    
    yields:
        - a line in the file."""

    with open(file) as f:
        for line in f:
            yield line