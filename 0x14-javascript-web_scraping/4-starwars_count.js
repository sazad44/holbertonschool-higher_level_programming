#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  try {
    let count = 0;
    if (error) {
      console.log(error);
    } else {
      for (let i = 0; i < JSON.parse(body)['results'].length; i++) {
        if (JSON.parse(body)['results'][i]['characters'].indexOf('https://swapi.co/api/people/18/') !== -1) {
          count += 1;
        }
      }
      console.log(count);
    }
  } catch (e) {
  }
});
