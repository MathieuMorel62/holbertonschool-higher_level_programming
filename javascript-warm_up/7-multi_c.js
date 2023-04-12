#!/usr/bin/node
/* Multiple printing of a string in JavaScript */

const numberOccurences = parseInt(process.argv[2]);

if (isNaN(numberOccurences)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numberOccurences; i++) {
    console.log('C is fun');
  }
}
