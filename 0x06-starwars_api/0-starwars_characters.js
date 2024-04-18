#!/usr/bin/node

const request = require('request');
const number = process.argv[2];

request(`https://swapi.dev/api/films/${number}`, async (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  if (res.statusCode === 200) {
    const film = JSON.parse(body);
    for (const element of JSON.parse(body).characters) {
      await new Promise((resolve, reject) => {
        request(element, (err, res, body2) => {
          if (err) {
            console.log(err);
            reject(err);
          }
          if (res.statusCode === 200) {
            const data2 = JSON.parse(body2);
            console.log(data2.name);
            resolve();
          }
        });
      });
    }
  }
});
