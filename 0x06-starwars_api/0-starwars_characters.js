#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/' + process.argv[2];

request(url, async function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).name);
  }
}
);
