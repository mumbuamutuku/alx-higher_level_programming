#!/usr/bin/node
const lst = require('./101-data').dict;
const ids = {};
for (const key in lst) {
  if (ids[lst[key]] === undefined) {
    ids[lst[key]] = [];
    ids[lst[key]].push(key);
  } else {
    ids[lst[key]].push(key);
  }
}
console.log(ids);
