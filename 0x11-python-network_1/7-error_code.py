#!/usr/bin/python3
"""Py script to print content of request or error code if above 400"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    try:
        if int(response.status_code) >= 400:
            response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as err:
        print("Error code: {}".format(response.status_code))
