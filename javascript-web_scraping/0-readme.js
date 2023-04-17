#!/usr/bin/node
/* Script that reads and prints the content of a file */

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data);
});
