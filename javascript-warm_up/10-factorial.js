#!/usr/bin/node

function factorial (i) {
  if (Number.isNaN(i) || i <= 1) {
    return 1;
  }
  return i * factorial(i - 1);
}

const arg = Number.parseInt(process.argv[2], 10);
console.log(factorial(arg));
