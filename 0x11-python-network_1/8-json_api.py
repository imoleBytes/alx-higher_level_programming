#!/usr/bin/python3
"""Module contains a main func that sends a POST request"""
import requests
import sys


def main():
    """Main Func"""
    url = 'http://0.0.0.0:5000/search_user'
    args_num = len(sys.argv)
    if args_num < 2:
        values = {'q': ""}
    else:
        values = {'q': sys.argv[1]}

    res = requests.post(url, data=values)

    try:
        res = res.json()
        if res == {}:
            print('No result')
        else:
            print(f"[{res['id']}] {res['name']}")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
