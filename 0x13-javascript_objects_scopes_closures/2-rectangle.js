#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0 && typeof w !== 'undefined') && (h > 0 && typeof h !== 'undefined')) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
