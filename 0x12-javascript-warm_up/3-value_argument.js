#!/usr/bin/node

const argv = process.argv;
let firstArg;

firstArg = argv[2];
if (firstArg === undefined){
  console.log('No argument');
}else {
	console.log(firstArg);
}
