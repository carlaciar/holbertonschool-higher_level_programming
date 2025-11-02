#!/usr/bin/node

const args = process.argv.slice(2);
const value = args[0];
const count = parseInt(args[0]);

if (isNaN(value)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
