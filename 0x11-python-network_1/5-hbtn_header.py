#!/usr/bin/python3
"""Module contains a main func that gets the X-Request-Id in the header"""
import requests
import sys


def main():
    """Main Func"""
    url = sys.argv[1]
    # "https://alx-intranet.hbtn.io/status"
    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
