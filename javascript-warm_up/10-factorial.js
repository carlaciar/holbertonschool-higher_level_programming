#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args[0]);

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1; // base case
  }
  return n * factorial(n - 1); // recursive call
}

console.log(factorial(num));
