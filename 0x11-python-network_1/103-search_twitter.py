#!/usr/bin/python3
"""Python script makes requests to the Twitter API with arguments"""
import requests
import base64
from sys import argv

if __name__ == "__main__":
    bD = 'grant_type=client_credentials'.encode('utf-8')
    cT = 'application/x-www-form-urlencoded;charset=UTF--8'
    secretKey = argv[1] + ":" + argv[2]
    secretKey = secretKey.encode('utf-8')
    secretKeyB64 = base64.b64encode(secretKey).decode('utf-8')
    headersC = {'authorization': 'Basic {}'.format(secretKeyB64),
                'content-type': cT}
    bearer = requests.post('https://api.twitter.com/oauth2/token',
                           headers=headersC,
                           data=bD).json()
    bToken = bearer['access_token']
    response = requests.get('https://api.twitter.com/1.1/search/tweets.json',
                            headers={'authorization': 'Bearer {}'
                                     .format(bToken)},
                            params={'q': argv[3].encode('utf-8')}).json()
    try:
        for i in range(5):
            id = response['statuses'][i]['id']
            text = response['statuses'][i]['text']
            name = response['statuses'][i]['user']['name']
            print("[{}] {} by {}".format(id, text, name))
    except:
        pass
