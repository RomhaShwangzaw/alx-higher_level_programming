#!/usr/bin/node
// This script prints all characters of a Star Wars movie:

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  // Printing the error if occurred
  if (error) console.log(`code: ${error}`);

  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) console.log(`code: ${error}`);
      else console.log(JSON.parse(body).name);
    });
  }
});
