#!/usr/bin/node
const args = process.argv;
console.log(add(parseInt(args[2], 10), parseInt(args[3], 10)));

function add (a, b) {
  return (a + b);
}
