#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args.length === 2) {
  console.log(1);
} else {
  const number = parseInt(args[2]);
  let output = 1;
  for (let i = 2; i <= number; i++) {
    output *= i;
  }
  console.log(output);
}
