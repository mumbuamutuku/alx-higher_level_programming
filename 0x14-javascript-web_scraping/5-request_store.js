#!/usr/bin/node
// Write a script that writes a string to a file.

const fs = require('fs');
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(process.argv[3], body, error => {
      if (error) {
        console.error(err);
      }
    });
  }
});
