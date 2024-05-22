#!/usr/bin/node
/**
 *  that prints the number of movies where the character “Wedge Antilles” is present.
 */
const request = require('request');

const url = process.argv[2];
let count = 0;
let characters;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;

    for (let i = 0; i < films.length; i++) {
      characters = films[i].characters;

      for (let a = 0; a < characters.length; a++) {
        if (characters[a].endsWith('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
