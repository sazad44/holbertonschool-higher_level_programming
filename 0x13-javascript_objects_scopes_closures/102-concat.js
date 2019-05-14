#!/usr/bin/node
const fs = require('fs');

fs.exists(process.argv[2], function(exists) {
  if (exists) {
    fs.stat(process.argv[2], function(error, stats) {
      let fd = fs.open(process.argv[2], 'r', function(error, fd) {
	var buffer = new Buffer.alloc(stats.size);
	fs.read(fd, buffer, 0, buffer.length, null, function(error, bytesRead, buffer) {
	  var data = buffer.toString('utf-8', 0, buffer.length);
	  fs.writeFile(process.argv[4], data, function (err) {
	    if (err) throw err;
	  })
	})
      })
    })
  }
})

fs.exists(process.argv[3], function(exists) {
  if (exists) {
    fs.stat(process.argv[3], function(error, stats) {
      let fd = fs.open(process.argv[3], 'r', function(error, fd) {
	var buffer = new Buffer.alloc(stats.size);
	fs.read(fd, buffer, 0, buffer.length, null, function(error, bytesRead, buffer) {
	  var data = buffer.toString('utf-8', 0, buffer.length);
	  fs.appendFile(process.argv[4], data, function (err) {
	    if (err) throw err;
	  })
	})
      })
    })
  }
})
