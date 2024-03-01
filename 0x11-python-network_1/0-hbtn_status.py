#!/usr/bin/python3
"""This module contains main func that sends a request"""
import urllib.request


def main():
    """Main func starts here"""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        msg = res.read()
    output = f"""\
Body response:
    - type: {type(msg)}
    - content: {msg}
    - utf8 content: {msg.decode()}"""
    print(output)


if __name__ == "__main__":
    main()
