#!/usr/bin/node
/**
 * this module gets the characters of a star war movie
 */
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function getCharacterName (url) {
  await request(url, (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      const name = JSON.parse(body).name;
      console.log(name);
    }
  });
}

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;

    for (let i = 0; i < characters.length; i++) {
      getCharacterName(characters[i]);
    }
  }
});
