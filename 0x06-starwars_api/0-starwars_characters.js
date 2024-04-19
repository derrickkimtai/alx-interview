#!/usr/bin/node

const request = require('request');

// Check if a movie ID was provided
if (process.argv.length < 3) {
  console.log('Please provide a movie ID as an argument.');
  process.exit(1);
}

const movieId = process.argv[2]; // Get the movie ID from the command-line argument
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`; // Construct the URL for the movie

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode);
    return;
  }

  if (body.characters && body.characters.length > 0) {
    body.characters.forEach(characterUrl => {
      // Extract the character ID from the URL
      const characterId = characterUrl.match(/\/api\/people\/(\d+)\//)[1];
      request(`https://swapi.dev/api/people/${characterId}/`, { json: true }, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error('Error:', response.statusCode);
          return;
        }

        console.log(body.name); // Print the character's name
      });
    });
  } else {
    console.log('No characters found for this movie.');
  }
});
