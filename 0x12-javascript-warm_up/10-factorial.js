#!/usr/bin/node
const args = process.argv;
console.log(factorial(parseInt(args[2], 10)));

function factorial (n) {
  if (n === 1 || !n) return (1);
  return (n * factorial(n - 1));
}
