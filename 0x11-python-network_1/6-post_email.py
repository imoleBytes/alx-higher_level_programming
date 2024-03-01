#!/usr/bin/python3
"""Module contains a main func that sends a POST request"""
import requests
import sys


def main():
    """Main Func"""
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    res = requests.post(url, data=values)
    print(res.content.decode('utf-8'))


if __name__ == "__main__":
    main()
