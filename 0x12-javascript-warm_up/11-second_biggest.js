#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  const list = [];
  for (let i = 2; i < args.length; i++) {
    list.push(parseInt(args[i]));
  }
  let firstMax = -Number.MAX_VALUE;
  let secondMax = -Number.MAX_VALUE;

  for (const element of list) {
    if (element > firstMax) {
      secondMax = firstMax;
      firstMax = element;
    } else if (element > secondMax) {
      secondMax = element;
    }
  }
  console.log(secondMax);
}
