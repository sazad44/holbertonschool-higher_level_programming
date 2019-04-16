#!/usr/bin/python3
"""Py script to list 10 commits of a repo"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url).json()
    try:
        for i in range(10):
            sha = response[i].get('sha')
            name = response[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, name))
    except IndexError:
        pass
