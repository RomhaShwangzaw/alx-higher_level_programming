#!/usr/bin/node
// This script computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  // Printing the error if occurred
  if (error) console.log(`code: ${error}`);

  const result = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0
  };
  const tasks = JSON.parse(body);
  for (const task of tasks) {
    if (task.completed) {
      // if (result.get(task.userId)) result[task.userId] += 1;
      // else result[task.userId] = 1;
      result[task.userId] += 1;
    }
  }

  console.log(result);
});
