#!/usr/bin/node
/* Script that prints all characters of a Star Wars movie */

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;
  let characterIndex = 0;

  function getNextCharacter () {
    request(characters[characterIndex], function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
      characterIndex++;
      if (characterIndex < characters.length) {
        getNextCharacter();
      }
    });
  }

  getNextCharacter();
});
