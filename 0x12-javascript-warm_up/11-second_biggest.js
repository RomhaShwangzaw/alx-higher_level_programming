#!/usr/bin/node
const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  const myArray = [];
  for (let i = 2; i < args.length; i++) {
    myArray.push(parseInt(args[i], 10));
  }
  myArray.sort();
  myArray.reverse();
  console.log(myArray[1]);
}
