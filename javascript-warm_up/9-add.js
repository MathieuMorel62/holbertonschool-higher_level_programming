#!/usr/bin/node
/* Script that prints the addition of 2 integers */

function add (a, b) {
  return a + b;
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  const result = add(a, b);
  console.log(result);
}
