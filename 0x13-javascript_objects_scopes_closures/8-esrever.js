#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  for (let i = 0, j = list.length - 1; j >= 0; i++, j--) {
    reverse[j] = list[i];
  }
  return (reverse);
};
