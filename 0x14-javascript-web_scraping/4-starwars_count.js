#!/usr/bin/node
// This script prints the number of movies where the
// character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  // Printing the error if occurred
  if (error) console.log(`code: ${error}`);

  let count = 0;
  const movies = JSON.parse(body).results;
  for (const movie of movies) {
    const characters = movie.characters;
    for (const character of characters) {
      if (character.includes('18')) count += 1;
    }
  }

  console.log(count);
});
