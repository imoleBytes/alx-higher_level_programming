#!/usr/bin/node

const size = process.argv[2];

if (isNaN(size) || size === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(size); i++) {
    console.log('X'.repeat(parseInt(size)));
  }
}
