#!/usr/bin/node
const request = require("request");

request(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (error, response, body) => {
    if (!error) {
      const film = JSON.parse(body);
      chars = film.characters;

      chars.forEach((char) => {
        request(char, (error, response, body) => {
          if (!error) {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      });
    }
  }
);
