#!/usr/bin/node
const impDict = require('./101-data').dict;

newDict = {};
Object.keys(impDict).map(x => { typeof newDict[impDict[x]] !== 'undefined' ? newDict[impDict[x]].push(x) : newDict[impDict[x]] = [x] });
console.log(newDict);
