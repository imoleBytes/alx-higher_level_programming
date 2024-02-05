#!/usr/bin/node

exports.esrever = function (list) {
  const revelis = [];

  for (let i = list.length - 1; i >= 0; i--) {
    revelis.push(list[i]);
  }
  return (revelis);
};
