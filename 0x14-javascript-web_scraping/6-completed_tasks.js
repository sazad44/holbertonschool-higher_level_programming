#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  let newDict = {};
  todoList = JSON.parse(body);
  Object.values(todoList).map(x => {
    if (typeof newDict[x['userId']] === 'undefined') newDict[x['userId']] = 0;
    if (x['completed'] === true) newDict[x['userId']] += 1;
  });
  console.log(JSON.stringify(newDict, null, 2));
});
