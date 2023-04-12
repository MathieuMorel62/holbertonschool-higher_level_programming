#!/usr/bin/node
/* Script that searches the second biggest integer in the list */

const args = process.argv.slice(2).map(Number);

function secondLargest (array) {
  const sortedArray = array.sort((a, b) => b - a);
  if (sortedArray.length < 2) {
    return 0;
  } else {
    return sortedArray[1];
  }
}

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  console.log(secondLargest(args));
}
