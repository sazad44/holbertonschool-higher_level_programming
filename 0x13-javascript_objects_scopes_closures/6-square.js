#!/usr/bin/node
const Square = require('./5-square');

Square.prototype.charPrint = function (c) {
  if (typeof c === 'undefined') {
    c = 'X';
  }
  for (let h = 0; h < this.height; h++) {
    let array = [];
    for (let w = 0; w < this.width; w++) {
      array.push(c);
    }
    console.log(array.join(''));
  }
}

module.exports = Square;
