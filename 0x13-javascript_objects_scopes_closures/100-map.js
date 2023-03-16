#!/usr/bin/node
const lst = require('./100-data').list;
console.log(lst);
const newList = lst.map((num, index) => num * index);
console.log(newList);
