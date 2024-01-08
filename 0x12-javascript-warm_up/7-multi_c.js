#!/usr/bin/node

const argv = process.argv;
const firstArg = argv[2];

if (firstArg === undefined || isNaN(firstArg)) {
	console.log('Missing number of occurrences');
}else if (parseInt(firstArg) <= 0) {
	;
}else{
	for (let i = 0; i < parseInt(firstArg); i++) {
		console.log('C is fun');
	}
}
