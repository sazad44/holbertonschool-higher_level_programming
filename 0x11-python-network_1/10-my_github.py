#!/usr/bin/python3
"""Py script takes github credentials and displays your id"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    resDict = response.json()
    print(resDict.get('id'))
