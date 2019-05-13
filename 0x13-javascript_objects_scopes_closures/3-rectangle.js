#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0 && typeof w !== 'undefined') && (h > 0 && typeof h !== 'undefined')) {
      this.width = w;
      this.height = h;
    }
    this.print = function () {
      for (let h = 0; h < this.height; h++) {
        for (let w = 0; w < this.width; w++) {
	  process.stdout.write('X');
        }
	process.stdout.write('\n')
      }
    };
  }
}

module.exports = Rectangle;
