#!/usr/bin/node
const process = require('process');
const args = process.argv;
let arg1, arg2;
arg1 = args[2];
arg2 = args[3];
console.log(arg1 + ' is ' + arg2);
