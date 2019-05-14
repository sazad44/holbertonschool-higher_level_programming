#!/usr/bin/node
const fs = require('fs');

fs.stat(process.argv[2], function (error, stats) {
  if (error) throw error;
  fs.open(process.argv[2], 'r', function (error, fd) {
    if (error) throw error;
    let buffer = new Buffer.Alloc(stats.size);
    fs.read(fd, buffer, 0, buffer.length, null, function (error, bytesRead, buffer) {
      if (error) throw error;
      let data = buffer.toString('utf-8', 0, buffer.length);
      fs.writeFile(process.argv[4], data, function (err) {
        if (err) throw err;
      });
    });
  });
});

fs.stat(process.argv[3], function (error, stats) {
  if (error) throw error;
  fs.open(process.argv[3], 'r', function (error, fd) {
    if (error) throw error;
    let buffer = new Buffer.Alloc(stats.size);
    fs.read(fd, buffer, 0, buffer.length, null, function (error, bytesRead, buffer) {
      if (error) throw error;
      let data = buffer.toString('utf-8', 0, buffer.length);
      fs.appendFile(process.argv[4], data, function (err) {
        if (err) throw err;
      });
    });
  });
});
