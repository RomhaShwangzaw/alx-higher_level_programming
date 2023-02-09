#!/usr/bin/node
// This script computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  // Printing the error if occurred
  if (error) console.log(`code: ${error}`);

  const result = {};
  const tasks = JSON.parse(body);
  for (const task of tasks) {
    if (task.completed) {
      if (result[task.userId] === undefined) result[task.userId] = 1;
      else result[task.userId]++;
    }
  }

  console.log(result);
});
