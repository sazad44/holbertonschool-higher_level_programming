#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  try {
    let count = 0;
    if (error) {
      console.log(error);
    } else {
      let results = JSON.parse(body)['results'];
      for (let i = 0; i < results.length; i++) {
        for (let c = 0; c < results[i]['characters'].length; c++) {
	  for (let ch = 0; ch < results[i]['characters'][c].length; ch++) {
	    if (results[i]['characters'][c].charAt(ch) === '1' && results[i]['characters'][c].charAt(ch + 1) === '8') {
              count += 1;
	    }
	  }
        }
      }
      console.log(count);
    }
  } catch (e) {
    console.log(e);
  }
});
