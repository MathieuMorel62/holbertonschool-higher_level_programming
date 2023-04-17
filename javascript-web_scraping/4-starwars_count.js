#!/usr/bin/node
/* Script that prints the number of movies */

const request = require('request');

const starWarsFilmsApiUrl = process.argv[2];
const CHARACTER_ID = '18';

request(starWarsFilmsApiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  const filmsWithCharacter = films.filter(film => {
    const characters = film.characters;
    return characters.some(character => character.includes(`/api/people/${CHARACTER_ID}/`));
  });

  const count = filmsWithCharacter.length;
  console.log(count);
});
