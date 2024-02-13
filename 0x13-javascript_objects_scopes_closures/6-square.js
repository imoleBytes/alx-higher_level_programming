#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    let ch;
    if (c) {
      ch = c;
    } else {
      ch = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(ch.repeat(this.width));
    }
  }
}

module.exports = Square;
