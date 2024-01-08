#!/usr/bin/node

const agr1 = process.argv[2];

function fact (num) {
  if (num <= 1) {
    return 1;
  }
  return num * fact(num - 1);
}

if (agr1 === undefined || isNaN(agr1)) {
  console.log(1);
} else {
  try {
    console.log(fact(parseInt(agr1)));
  } catch (error) {
    console.log(1);
  }
}
