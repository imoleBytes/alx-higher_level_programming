#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""
# 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 (its revoked!)
import requests
import sys


def main():
    """Main Func"""
    repos = sys.argv[1]
    user = sys.argv[2]
    url = f'https://api.github.com/repos/{user}/{repos}/commits'

    r = requests.get(url).json()[-10:]
    r.reverse()

    for i in r:
        sha = i.get('sha')
        author_name = i['commit']['author']['name']
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    main()
