#!/usr/bin/python3
"""Py script to fetch commandline url and return request id"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('x-request-id'))
