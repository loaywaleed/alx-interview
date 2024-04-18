#!/usr/bin/node

const request = require('request');
const number = process.argv[2];

request(`https://swapi.dev/api/films/${number}`, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  if (res.statusCode === 200) {
    const film = JSON.parse(body);
    const charactersUrls = film.characters;
    console.log(film.title);
    charactersUrls.forEach(element => {
      request(element, (err, res, body2) => {
        if (err) {
          console.log(err);
          return err;
        }
        if (res.statusCode === 200) {
          const data2 = JSON.parse(body2);
          console.log(data2.name);
        }
      });
    });
  }
});
