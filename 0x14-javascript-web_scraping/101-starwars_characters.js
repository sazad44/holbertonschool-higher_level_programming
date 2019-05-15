#!/usr/bin/node
const request = require('request');

function reqAgain (i, characters, retDict) {
  if (i === characters.length) return retDict;
  request(characters[i], function (error, response, body) {
    if (error) console.log(error);
    console.log(JSON.parse(body)['name']);
    reqAgain(i + 1, characters, retDict);
  });
}

function reqResolution (filmNo) {
  request('http://swapi.co/api/films/' + filmNo, function (error, response, body) {
    if (error) console.log(error);
    let characters = JSON.parse(body)['characters'];
    reqAgain(0, characters, {});
  });
}

reqResolution(process.argv[2]);
