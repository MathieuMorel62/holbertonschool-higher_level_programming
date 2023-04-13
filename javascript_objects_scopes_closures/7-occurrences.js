#!/usr/bin/node
/* Add implementation of nbOccurences function */

exports.nbOccurences = function (list, searchElement) {
  let countOccurences = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      countOccurences += 1;
    }
  }
  return countOccurences;
};
