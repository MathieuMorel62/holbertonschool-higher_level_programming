#!/usr/bin/node
/* Converts a number from base 10 to another base */

exports.converter = function (base) {
  return function (num) {
    return parseInt(num, 10).toString(base);
  };
};
