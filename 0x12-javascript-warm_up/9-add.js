#!/usr/bin/node

let sum;

function add (a, b) {
  return a + b;
}

const num1 = process.argv[2];
const num2 = process.argv[3];

if ((num1 === undefined) || (num2 === undefined)) {
  console.log('NaN');
} else if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  sum = add(parseInt(num1), parseInt(num2));
  console.log(sum);
}
