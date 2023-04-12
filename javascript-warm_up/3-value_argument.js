#!/usr/bin/node
/* Script that prints the first argument passed */

const firstArg = process.argv[2];

if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
