#!/usr/bin/node
const process = require('process');
const args = process.argv;

const number = Number(args[2]);
if (number) {
  for (let i = 0; i < number; i++) {
    console.log('x'.repeat(number));
  }
} else {
  console.log('Missing size');
}
