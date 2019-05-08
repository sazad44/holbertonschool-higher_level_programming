#!/usr/bin/node
let maxOne = Number.MIN_VALUE;
let maxTwo = Number.MIN_VALUE;
if (process.argv.length < 4) {
  console.log(0);
} else {
  for (let i = 0; i < process.argv.length; i++) {
    if (process.argv[i] > maxOne) {
      maxTwo = maxOne;
      maxOne = process.argv[i];
    }
  }
  if (maxTwo !== Number.MIN_VALUE) {
    console.log(maxTwo);
  } else {
    console.log(0);
  }
}
