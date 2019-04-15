#!/usr/bin/python3
"""Displays value of X-Request-Id for HTTP Response"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.info().get('X-Request-Id'))
