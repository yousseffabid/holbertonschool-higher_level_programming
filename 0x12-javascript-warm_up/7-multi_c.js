#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args.length === 2) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log('C is fun');
  }
}
