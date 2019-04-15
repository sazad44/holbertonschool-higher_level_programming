#!/usr/bin/python3
"""Py script to take URL and return response body and handle errors"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
