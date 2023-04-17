#!/usr/bin/node
/* Script that prints the number of movies */

const request = require('request');

const starWarsFilmsApiUrl = process.argv[2];
const CHARACTER_ID = '18';

request(starWarsFilmsApiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    for (let i = 0; i < films.length; i++) {
      const characters = films[i].characters;
      if (characters.includes(`https://swapi-api.hbtn.io/api/people/${CHARACTER_ID}/`)) {
        count++;
      }
    }
    console.log(count);
  }
});
