#!/usr/bin/node
/* Add charPrint method to Square class */

const lastSquare = require('./5-square');

class Square extends lastSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
