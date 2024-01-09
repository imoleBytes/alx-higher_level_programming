#!/usr/bin/node

const Square5 = require("./5-square");

class Square extends Square5{
	charPrint(c) {
		let sym = c;
		if (c === undefined) {
			c = 'X';
		}
		for (let i = 0; i < this.height; i++) {
			console.log(sym.repeat(this.width));
		}
	};
};

module.exports = Square;
