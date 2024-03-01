#!/usr/bin/python3
"""Module contains a main func that gets the X-Request-Id"""
import urllib.request
import urllib.parse
import sys


def main():
    """Main Func"""
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))


if __name__ == "__main__":
    main()
