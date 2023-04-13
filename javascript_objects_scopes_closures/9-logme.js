#!/usr/bin/node
/* Function that prints the number of arguments already printed */

let countArgs = 0;
exports.logMe = function (item) {
  console.log(countArgs + ': ' + item);
  countArgs += 1;
};
