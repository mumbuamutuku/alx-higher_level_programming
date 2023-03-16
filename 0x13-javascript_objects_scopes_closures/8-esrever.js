#!/usr/bin/node
exports.esrever = function (list) {
  const f = [];
  for (let i = list.length - 1; i >= 0; i--) {
    f.push(list[i]);
  }
  return f;
};
