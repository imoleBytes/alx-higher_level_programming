#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.request
import urllib.error


def main():
    """Func starts here!"""
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            data = res.read().decode('utf-8')
            print(data)
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")


if __name__ == "__main__":
    main()
