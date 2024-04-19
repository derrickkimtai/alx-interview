#!/usr/bin/node

const request = require('request');

function printMovieCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request(url, function (error, response, body) {
    if (error) {
      console.error('Error:', error);
      return;
    }

    const data = JSON.parse(body);
    const characters = data.characters;

    if (characters) {
      characters.forEach((characterUrl) => {
        request(characterUrl, function (error, response, body) {
          if (error) {
            console.error('Error:', error);
            return;
          }

          const characterName = JSON.parse(body).name;
          console.log(characterName);
        });
      });
    } else {
      console.error('No characters found for this movie');
    }
  });
}

const movieId = process.argv[2];
printMovieCharacters(movieId);
