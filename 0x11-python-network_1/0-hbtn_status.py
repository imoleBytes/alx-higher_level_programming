#!/usr/bin/python3
"""This module contains main func that sends a request"""
import urllib.request


def main():
    """Main func starts here"""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        msg = res.read()
    print("Body response:")
    print(f"\t- type: {type(msg)}")
    print(f"\t- content: {msg}")
    print(f"\t- utf8 content: {msg.decode()}")


if __name__ == "__main__":
    main()
