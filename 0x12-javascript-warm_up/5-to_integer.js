#!/usr/bin/node
const args = process.argv;
const value = parseInt(args[2], 10);
if (value) {
  console.log('My number: ' + value);
} else {
  console.log('Not a number');
}
