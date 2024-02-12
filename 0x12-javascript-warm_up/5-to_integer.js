#!/usr/bin/node

const argv = process.argv;
let num = parseInt(argv[2]);

if (!num)
{
    console.log("Not a number");
}
else
{
console.log(`My number: ${num}`);
}
