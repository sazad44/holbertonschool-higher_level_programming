#!/usr/bin/python3
"""Fetches url response"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as u:
        print('Body response:')
        response = u.read()
        print('    - type: {}'.format(type(response)))
        print('    - content: {}'.format(response))
        print('    - utf8 content: {}'.format(response.decode('utf-8')))
