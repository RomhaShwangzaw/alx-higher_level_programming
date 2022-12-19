#!/usr/bin/node
const args = process.argv;
const size = parseInt(args[2], 10);
if (size) {
  for (let x = 0; x < size; x++) {
    let row = '';
    for (let y = 0; y < size; y++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
