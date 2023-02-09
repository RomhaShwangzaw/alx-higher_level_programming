#!/usr/bin/node
// This script prints the title of a Star Wars movie
// where the episode number matches a given integer.

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  // Printing the error if occurred
  if (error) console.log(`code: ${error}`);

  // Printing the title of the movie
  console.log(JSON.parse(body).title);
});
