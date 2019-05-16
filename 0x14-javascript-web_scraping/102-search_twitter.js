#!/usr/bin/node
const base64 = require('base-64');
const request = require('request');

let keyCombo = process.argv[2] + ':' + process.argv[3];
let keyComboEncode = encodeURI(keyCombo);
let keyComboEncode64 = base64.encode(keyComboEncode);
let bearerToken = '';
let respDict = {};
let tweetDict = {};
request.post({ url: 'https://api.twitter.com/oauth2/token', headers: { 'Authorization': 'Basic ' + keyComboEncode64, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' }, body: 'grant_type=client_credentials' }, (error, response, body) => {
  if (error) console.log(error);
  respDict = JSON.parse(body);
  if (respDict.token_type !== 'bearer') console.log(respDict + 'HEY THIS ISNT THE RIGHT TOKEN');
  bearerToken = respDict.access_token;
  request({ url: 'https://api.twitter.com/1.1/search/tweets.json',
    headers: { 'Authorization': 'Bearer ' + bearerToken },
    qs: { 'q': process.argv[4] }
  }, (error, response, body) => {
    if (error) console.log(error);
    tweetDict = JSON.parse(body);
    for (let i = 0; i < 5; i++) {
      let status = tweetDict.statuses[i];
      let output = '[' + status.user.id + '] ' + status.text + ' by ' + status.user.screen_name;
      console.log(output);
    }
  });
});
