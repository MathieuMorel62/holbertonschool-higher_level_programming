#!/usr/bin/node
/* Script that prints the number of movies */

const request = require('request');

const starWarsFilmsApiUrl = process.argv[2];

request(starWarsFilmsApiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  }

  const films = JSON.parse(body).results;

  const wedgeAntillesFilms = films.filter(function (film) {
    const charactersUrl = film.characters;
    const wedgeAntilleUrl = "https://swapi-api.hbtn.io/api/people/18/";
    const wedgeAntillesIsPresent = charactersUrl.includes(wedgeAntilleUrl);
    return wedgeAntillesIsPresent;
  });

  const numberOfWedgeAntillesFilms = wedgeAntillesFilms.length;
  console.log(numberOfWedgeAntillesFilms);
});
