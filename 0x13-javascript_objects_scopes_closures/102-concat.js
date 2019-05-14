#!/usr/bin/node
const fs = require('fs');

fs.stat(process.argv[2], function (error, stats) {
  if (error) throw error;
  fs.open(process.argv[2], 'r', function (error, fd) {
    if (error) throw error;
    fs.readFile(process.argv[2], function read (err, data) {
      if (err) throw err;
      let fa = data.toString('utf-8', 0, stats.size);
      fs.writeFile(process.argv[4], fa, function (err) {
        if (err) throw err;
      });
    });
  });
});

fs.stat(process.argv[3], function (error, stats) {
  if (error) throw error;
  fs.open(process.argv[3], 'r', function (error, fd) {
    if (error) throw error;
    fs.readFile(process.argv[3], function read (err, data) {
      if (err) throw err;
      let fa = data.toString('utf-8', 0, stats.size);
      fs.appendFile(process.argv[4], fa, function (err) {
        if (err) throw err;
      });
    });
  });
});
