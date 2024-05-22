#!/usr/bin/node
/**
 * this module gets the title of a star war movie
 */
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const title = JSON.parse(body).title;
    console.log(`${title}`);
  }
});
