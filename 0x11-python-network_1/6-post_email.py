#!/usr/bin/python3
"""Py script to send post request to url with email argument and display"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.post(argv[1], data={'email': "{}".format(argv[2])})
    print(response.text)
