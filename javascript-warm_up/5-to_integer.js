#!/usr/bin/node

const args = process.argv.slice(2);
const value = args[0];

if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(value));
}
