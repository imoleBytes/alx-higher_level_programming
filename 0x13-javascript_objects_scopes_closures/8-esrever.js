#!/usr/bin/node

exports.esrever = function (list) {
	let revelis = [];

	for (let i = list.length - 1; i >= 0; i--) {
		revelis.push(list[i]);
	}
	return (revelis)
};
