#!/usr/bin/node
const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  let characters = JSON.parse(body)['characters'];
  characterKeys = Object.keys(characters);
  for (let i = 0; i < characterKeys.length; i++) {
    console.log(characters[i]);
    request(characters[characterKeys[i]], function (error, response, body) {
      if (error) console.log(error);
      console.log(JSON.parse(body)['name']);
    });
  };
});
