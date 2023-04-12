#!/usr/bin/node
/* Integer argument conversion */

const firstArg = process.argv[2];
const integer = parseInt(firstArg, 10);

if (isNaN(integer)) {
  console.log('Not a number');
} else {
  console.log('My number:', integer);
}
