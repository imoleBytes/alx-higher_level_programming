#!/usr/bin/node
/**
 * this module reads a file
 */
const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    // console.log(data);
    console.log(data.toString('utf-8'));
  }
});
