#!/usr/bin/node
const total = { amount: 0 };
exports.logMe = function (item) {
  console.log(total.amount + ': ' + item);
  total.amount = total.amount + 1;
};
