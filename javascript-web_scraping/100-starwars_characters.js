#!/usr/bin/node
/* Script that prints all characters of a Star Wars movie */

const request = require('request');

const movieId = process.argv[2];
const filmApiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(filmApiUrl, function (filmError, filmResponse, filmBody) {
  if (filmError) {
    console.log(filmError);
  } else {
    const filmData = JSON.parse(filmBody);

    for (const characterApiUrl of filmData.characters) {
      request(characterApiUrl, function (characterError, characterResponse, characterBody) {
        if (characterError) {
          console.error(characterError);
        } else {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        }
      });
    }
  }
});
