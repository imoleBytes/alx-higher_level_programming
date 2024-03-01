#!/usr/bin/python3
"""Module contains a main func that sends that authenticate
into github and get the id of the user
"""
# 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
import requests
import sys


def main():
    """Main Func"""
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    paswd = sys.argv[2]

    r = requests.get(url, auth=(user, paswd))
    print(r.json().get('id'))
    # print(r.json().get('name'))


if __name__ == "__main__":
    main()
