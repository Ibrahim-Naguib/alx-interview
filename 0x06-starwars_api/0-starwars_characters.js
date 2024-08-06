#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    printChars(characters, 0);
  }
});

const printChars = (chars, index) => {
  request.get(chars[index], (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      const name = JSON.parse(body).name;
      console.log(name);
      if (index + 1 < chars.length) {
        printChars(chars, index + 1);
      }
    }
  });
};
