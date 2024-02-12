#!/usr/bin/node

const argv = process.argv;

if (isNaN(argv[2])) {
  console.log(1);
} else {
  const result = factorial(parseInt(argv[2]));
  console.log(result);
}

function factorial (num) {
  if (num < 2) {
    return (1);
  }
  return num * factorial(num - 1);
}
