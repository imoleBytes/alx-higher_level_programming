#!/usr/bin/python3
"""Module contains a main func that fetches a url"""
import requests


def main():
    """Main Func"""
    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url)
    msg = res.content.decode('utf-8')
    output = f"""Body response:
    - type: {type(msg)}
    - content: {msg}"""
    print(output)
    # print(dir(res))


if __name__ == "__main__":
    main()
