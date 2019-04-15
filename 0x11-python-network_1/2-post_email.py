#!/usr/bin/python3
"""Sends POST request to url and email specified in command line"""
import urllib
import urllib.parse
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    data = urllib.parse.urlencode({'email':argv[2]}).encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
