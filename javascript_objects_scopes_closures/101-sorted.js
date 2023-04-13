#!/usr/bin/node
/* Script that imports a dictionary of occurrences by user id */

const dict = require('./101-data.js').dict;

const newDict = {};
for (const userId in dict) {
  const occurrences = dict[userId];
  if (occurrences in newDict) {
    newDict[occurrences].push(userId);
  } else {
    newDict[occurrences] = [userId];
  }
}

console.log(newDict);
