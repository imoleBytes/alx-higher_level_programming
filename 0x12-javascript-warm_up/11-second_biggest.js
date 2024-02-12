#!/usr/bin/node

const argv = process.argv;

if (argv.length <= 3) {
  console.log('0');
} else {
  const arr = argv.slice(2).map(Number);
  const sec = arr.sort((a, b) => b - a)[1];
  console.log(sec);
}

// let argv = process.argv.slice(2);
// const len = argv.length;

// if (len < 2) {
//   console.log('0');
// } else {
//   argv = argv.map(Number).sort(); // sort in ascending order
//   console.log(argv[len - 2]);
// }
