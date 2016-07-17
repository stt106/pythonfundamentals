#!/usr/bin/env python3

"""Retrieve and print words from a URL


Usage:


    py -3 words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words():
    """Fetch words from a given URL
    
    Args:
        url : The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from the document.
    """
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                words.append(word)
    return words


def print_items(items):
    """Print each item on a line

    Args:
        items : an iterable series of printable items.  
    """
    for item in items:
        print(item)


def main():
    words = fetch_words()
    print_items(words)


# to make sure the script can be imported as a module and can be executed as a script
# Python runtime defines some attributes which are delimited by double underscore
if __name__ == '__main__':
    main()