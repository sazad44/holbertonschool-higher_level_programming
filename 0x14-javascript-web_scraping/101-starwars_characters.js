#!/usr/bin/node
const request = require('request');

const retDict = {};

function repAgain (idx, length, url) {
  if (idx >= length) {
  } else {
    request(url[idx], function (error, response, body) {
      console.log(JSON.parse(body)['name']);
    });
  }
}

function reqAgain (idx, length, url, repAgain) {
  if (idx >= length) {
  } else {
    console.log('WOWOWOWOW' + url[idx]);
    console.log('WOWOWOWOW' + url[idx + 1]);
    request(url[idx], function (error, response, body) {
      console.log(JSON.parse(body)['name']);
    });
    repAgain();
  }
}

function reqResolution(filmNo) {
  request('http://swapi.co/api/films/' + filmNo, function (error, response, body) {
    if (error) console.log(error);
    let characters = JSON.parse(body)['characters'];
    for (let i = 0; i < characters.length; i++) {
      reqAgain(i, characters.length, characters, reqAgain (i + 1, characters.length, characters));
    };
  });
}

reqResolution(process.argv[2]);
