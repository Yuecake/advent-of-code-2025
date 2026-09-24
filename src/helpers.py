"""Module containing helper functions for Advent of Code puzzles."""

from collections.abc import Iterator

def read_file(file: str) -> Iterator[str]:
    """Opens a file and returns the contents.
    
    returns:
        - the contents of a file."""
    with open(file) as f:
        return f.read()

def read_file_lines(file: str) -> Iterator[str]:
    """Opens a given file and yields each line as needed.
    
    yields:
        - a line in the file."""

    for line in read_file(file).splitlines():
        yield line

def read_file_comma_separated_values(file: str) -> Iterator[str]:
    """Yields each value separated by a comma.
    
    yields:
        - a comma separated value in the file."""

    for value in read_file(file).split(','):
        yield value