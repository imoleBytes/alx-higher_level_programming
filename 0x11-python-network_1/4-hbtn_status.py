#!/usr/bin/python3
"""Module contains a main func that fetches a url"""
import requests


def main():
    """Main Func"""
    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url)
    msg = res.content.decode('utf-8')
    print("Body response:")
    print(f'\t- type: {type(msg)}')
    print(f'\t- content: {msg}')


if __name__ == "__main__":
    main()
