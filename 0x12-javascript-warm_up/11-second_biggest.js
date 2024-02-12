#!/usr/bin/node

let argv = process.argv.slice(2);
const len = argv.length;

if (len < 3) {
  console.log('0');
} else {
  argv = argv.map(Number).sort(); // sort in ascending order
  console.log(argv[len - 2]);
}
