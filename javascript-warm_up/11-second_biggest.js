#!/usr/bin/node

const args = process.argv.slice(2);
const nums = args.map(Number);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  nums.sort((a, b) => b - a);
  console.log(nums[1]);
}
