#!/usr/bin/node
const c = process.argv.length;
console.log(c === 2 ? 'No argument' : c === 3 ? 'Argument found' : 'Arguments found');
