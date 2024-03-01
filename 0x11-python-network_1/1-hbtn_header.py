#!/usr/bin/python3
"""Module contains a main func that gets the X-Request-Id"""
import urllib.request
import sys


def main():
    """Main Func"""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        print(res.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
