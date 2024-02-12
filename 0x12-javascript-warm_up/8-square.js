#!/usr/bin/node

const argv = process.argv;
let size = argv[2];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  size = parseInt(size);

  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
