#!/usr/bin/node
/**
 * this module writes to a file
 */
const fs = require('fs');

const filePath = process.argv[2];
const str = process.argv[3];

fs.writeFile(filePath, str, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
