#!/usr/bin/node

const argInInt = Number.parseInt(process.argv[2], 10);

if (!Number.isNaN(argInInt)) {
  console.log(`My number: ${argInInt}`);
} else {
  console.log('Not a number');
}
