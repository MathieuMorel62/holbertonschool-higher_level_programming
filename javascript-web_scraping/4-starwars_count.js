#!/usr/bin/node
/* Script that prints the number of movies */

const request = require('request');

const starWarsFilmsApiUrl = 'https://swapi-api.hbtn.io/api/films/';

request(starWarsFilmsApiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  }

  const films = JSON.parse(body).results;

  const wedgeAntillesFilms = films.filter(function (film) {
    const charactersUrl = film.characters;
    const wedgeAntilleUrl = 'https://swapi-api.hbtn.io/api/people/18/';
    return charactersUrl.includes(wedgeAntilleUrl);
  });

  console.log(wedgeAntillesFilms.length);
});
