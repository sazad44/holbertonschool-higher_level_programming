#!/usr/bin/python3
"""Py script to print content of request or error code if above 400"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    if int(response.status_code) >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
