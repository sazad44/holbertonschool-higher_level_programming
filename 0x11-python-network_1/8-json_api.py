#!/usr/bin/python3
"""Py script to take in a letter and send a POST request returning JSON info"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        if len(argv) > 1:
            q = argv[1]
        else:
            q = ""
        url = 'http://0.0.0.0:5000/search_user'
        response = requests.post(url, data={'q': q})
        responseDict = response.json()
        if len(responseDict.keys()) == 0:
            print("No result")
        else:
            id = responseDict.get('id')
            name = responseDict.get('name')
            print("[{}] {}".format(id, name))
    except ValueError:
        print("Not a valid JSON")
