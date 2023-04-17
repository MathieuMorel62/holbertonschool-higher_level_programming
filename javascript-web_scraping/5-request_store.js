#!/usr/bin/node
/* Script that gets the contents of a webpage and stores it in a file */

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  fs.writeFile(file, body, 'utf8', function (error) {
    if (error) {
      console.error(error);
    }
  });
});
