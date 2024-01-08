#!/usr/bin/node

const lenghtOfArgv = process.argv.length;

if (lenghtOfArgv < 3) {
  console.log('No argument');
} else if (lenghtOfArgv === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
