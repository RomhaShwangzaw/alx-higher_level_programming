#!/usr/bin/node
const args = process.argv;
const value = parseInt(args[2], 10);
if (value) {
  for (let x = 0; x < value; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
