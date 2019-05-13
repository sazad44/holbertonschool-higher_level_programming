#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0 && typeof w !== 'undefined') && (h > 0 && typeof h !== 'undefined')) {
      this.width = w;
      this.height = h;
    }
  }
  // Prints the rectangle based on dimensions
  print () {
    for (let h = 0; h < this.height; h++) {
      let array = [];
      for (let w = 0; w < this.width; w++) {
        array.push('X');
      }
      console.log(array.join(''));
    }
  }
  // Swaps the values of height and width
  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
  // Doubles dimensions of rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  // Prints square with specified character
  charPrint (c) {
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
}

module.exports = Rectangle;
module.exports = Square;
