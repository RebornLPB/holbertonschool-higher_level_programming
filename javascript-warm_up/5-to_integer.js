#!/usr/bin/node

const argInInt = parseInt(process.argv[3]);

if (argInInt) {
  console.log(`My number: ${argInInt}`);
} else {
  console.log('Not a number');
}
