#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, function (error, response, body) {
  if (error) {
    console.error(error); // Print the error if one occurred
  } else {
    console.log(JSON.parse(body).title);
  }
});
