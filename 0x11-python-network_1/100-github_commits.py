#!/usr/bin/python3
"""Py script to list 10 commits of a repo"""
import requests
from sys import argv

if __name__ == "__main__":
    resDict = {}
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[1], argv[2])
    response = requests.get(url).json()
    for i in range(10):
        sha = response[i].get('sha')
        name = response[i].get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
