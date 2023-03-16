#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let shape = '';
    for (let w = 0; w < this.width; w++) {
      shape = shape + c;
    }
    for (let h = 0; h < this.height; h++) {
      console.log(shape);
    }
  }
}

module.exports = Square;
