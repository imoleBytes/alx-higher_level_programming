#!/usr/bin/node
/**
 * this module gets the characters of a star war movie
 */
const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    printName(characters, 0);
  }
});

function printName (characters, index) {
  request(characters[index], function (err, res, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printName(characters, index + 1);
      }
    }
  });
}
