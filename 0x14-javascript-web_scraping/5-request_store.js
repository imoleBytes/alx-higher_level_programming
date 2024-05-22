#!/usr/bin/node
/**
 * a script that gets the contents of a webpage and
 * stores it in a file.
 */
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFileSync(file, body, 'utf-8');
  }
});
