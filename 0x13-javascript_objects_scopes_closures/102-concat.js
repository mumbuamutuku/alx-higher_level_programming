#!/usr/bin/node
const fs = require('fs');

const file1 = (fs.readFileSync(process.argv[2])).toString();

const file2 = (fs.readFileSync(process.argv[3])).toString();

const content = file1 + file2;
fs.writeFile(process.argv[4], content, function (err) {
  if (err) throw err;
});
