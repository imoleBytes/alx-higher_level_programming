#!/usr/bin/node

let argv = process.argv.slice(2);
const len = argv.length;

if (len < 2) {
  console.log(0);
} else {
  argv = argv.sort(); // sort in ascending order
  console.log(argv[len - 2]);
}
