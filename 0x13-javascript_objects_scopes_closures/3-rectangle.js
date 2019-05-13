#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0 && typeof w !== 'undefined') && (h > 0 && typeof h !== 'undefined')) {
      this.width = w;
      this.height = h;
    }
  }
  // Method
  print () {
    for (let h = 0; h < this.height; h++) {
      let array = [];
      for (let w = 0; w < this.width; w++) {
        array.push('X');
      }
      console.log(array.join(''));
    }
  }
}

module.exports = Rectangle;
