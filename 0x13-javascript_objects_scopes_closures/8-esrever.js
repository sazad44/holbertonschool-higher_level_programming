#!/usr/bin/node

exports.esrever = function (list) {
  let newArr = [];
  for (let i = (list.length - 1); i >= 0; i -= 1) {
    newArr.push(list[i]);
  }
  return (newArr);
};
