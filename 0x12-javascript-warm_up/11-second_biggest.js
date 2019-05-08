#!/usr/bin/node
let maxOne = Number.MIN_SAFE_INTEGER;
let maxTwo = Number.MIN_SAFE_INTEGER;
if (process.argv.length < 4) {
  console.log(0);
} else {
  for (let i = 0; i < process.argv.length; i++) {
    if (Number(process.argv[i]) > maxOne) {
      maxTwo = maxOne;
      maxOne = Number(process.argv[i]);
    } else if (Number(process.argv[i]) > maxTwo) {
      maxTwo = Number(process.argv[i]);
    }
  }
  if (maxTwo !== Number.MIN_VALUE) {
    console.log(maxTwo);
  } else {
    console.log(maxOne);
  }
}
