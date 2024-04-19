#!/usr/bin/node

const util = require('util');
const request = util.promisify(require('request'));
const movie = process.argv[2];

async function getCharacter (movie) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + movie;
  const response = await request(url);
  const characters = JSON.parse(response.body).characters;
  for (const character of characters) {
    const res = await request(character);
    console.log(JSON.parse(res.body).name);
  }
}

getCharacter(movie);
