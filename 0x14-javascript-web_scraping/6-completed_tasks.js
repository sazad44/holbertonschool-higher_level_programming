#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  let newDict = {};
  let todoList = JSON.parse(body);
  Object.values(todoList).map(x => {
    if (typeof newDict[x['userId']] === 'undefined' && x['completed'] === true) newDict[x['userId']] = 1;
    if (x['completed'] === true) newDict[x['userId']] += 1;
  });
  console.log(newDict);
});
