# Making use of command line argument sys.argv
"""Retrive and print words from a url

Usage:
    python CommandLineArgument.py <URL>
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words froma a URL

    Args:
        url: The URL of a UTF-8 encoded text.

    Returns:
        A list of strings containing all the words of the text file.
    """

    story = urlopen(url)                  # Get the words from a URL
    story_words = []
    # print("story format: {}".format(type(story)))
    for line in story:                                                  # HTTP byte response
        line_words = line.decode('utf-8').split()                       # List type
        for word in line_words:                                         # Strings
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    """ Print items one per line.

    Args:
        items: A iterable series of printable print_items.

    Returns
        None
    """
    for item in items:
        print(item)

def main(url):
    # Using sys.argv to fetch the input url from command line
    """ Print each word from a text encoded document from URL

     Args:
        url: The url of the UTF-8 encoded text file
    """
    words = fetch_words(url)
    print_items(words)

if "__main__" == __name__ :
    print(sys.argv[0])
    main(sys.argv[1])


""" More information at arg parse module"""
