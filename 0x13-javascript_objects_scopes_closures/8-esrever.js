#!/usr/bin/node

exports.esrever = function (list) {
  new_arr = [];
  for (let i = (list.length - 1); i >= 0; i -= 1) {
    new_arr.push(list[i]);
  }
  return (new_arr);
};
