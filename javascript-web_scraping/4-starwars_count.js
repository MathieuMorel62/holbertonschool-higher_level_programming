#!/usr/bin/node
/* Script that prints the number of movies */

const request = require('request');

const starWarsFilmsApiUrl = process.argv[2];

request(starWarsFilmsApiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      const characters = film.characters;
      if (characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count++;
      }
    });
    console.log(count);
  }
});
