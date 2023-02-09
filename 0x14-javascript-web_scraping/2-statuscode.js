#!/usr/bin/node
// This script displays the status code of a GET request.

const request = require('request');
request(process.argv[2], (error, response) => {
  // Printing the error if occurred
  if (error) console.log(`code: ${error}`);

  // Printing status code
  console.log(`code: ${response.statusCode}`);
});
