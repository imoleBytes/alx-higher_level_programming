#!/usr/bin/node

class Rectangle {
	w;
	h;
	constructor(w, h){
		if ((w > 0) && (h > 0)) {
			this.width = w;
			this.height = h;
		}
	}
};

module.exports = Rectangle;
