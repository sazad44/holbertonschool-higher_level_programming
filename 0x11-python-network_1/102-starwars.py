#!/usr/bin/python3
"""Py script to take in string and send search request to SWAPI"""
import requests
from sys import argv

if __name__ == "__main__":
    urlSearch = "https://swapi.co/api/people/?search={}".format(argv[1])
    response = requests.get(urlSearch).json()
    resCount = response.get('count')
    print("Number of results: {}".format(resCount))
    while urlSearch is not None:
        response = requests.get(urlSearch).json()
        resCount = response.get('count')
        resResults = response.get('results')
        for d in resResults:
            print("{}".format(d.get("name")))
            filmUrls = d.get("films")
            for film in filmUrls:
                filmResponse = requests.get(film).json()
                print("\t{}".format(filmResponse.get('title')))
        urlSearch = response['next']
