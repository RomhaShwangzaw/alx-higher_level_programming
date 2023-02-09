#!/usr/bin/node
// This script gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  // Printing the error if occurred
  if (error) console.log(`code: ${error}`);

  fs.writeFile(filePath, body, 'utf-8', function (err) {
    if (err) console.log(err);
  });
});
