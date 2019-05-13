#!/usr/bin/python3
"""Py script to take in string and send search request to SWAPI"""
import requests
from sys import argv

if __name__ == "__main__":
    urlSearch = "https://swapi.co/api/people/?search={}".format(argv[1])
    response = requests.get(urlSearch)
    responseDict = response.json()
    resCount = responseDict.get('count')
    resResults = responseDict.get('results')
    print("Number of results: {}".format(resCount))
    for d in resResults:
        print("{}".format(d.get("name")))
