#!/usr/bin/node
(function add(a, b) {
  console.log(Number(a) + Number(b));
})(process.argv[2], process.argv[3]);
