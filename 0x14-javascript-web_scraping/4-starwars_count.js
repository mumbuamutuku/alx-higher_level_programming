#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error); // Print the error if one occurred
  } else {
    let antilles = 0;
    for (const film in JSON.parse(body).results) {
      for (const link in JSON.parse(body).results[film].characters) {
        if (JSON.parse(body).results[film].characters[link].split('/')[5] === '18') {
          antilles += 1;
        }
      }
    }
    console.log(antilles);
  }
});
