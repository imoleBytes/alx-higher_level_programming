#!/usr/bin/python3
"""Module contains a main func that gets the body or print status code"""
import requests
import sys


def main():
    """Main Func"""
    url = sys.argv[1]

    res = requests.get(url)
    print(res.content.decode('utf-8'))
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")


if __name__ == "__main__":
    main()
