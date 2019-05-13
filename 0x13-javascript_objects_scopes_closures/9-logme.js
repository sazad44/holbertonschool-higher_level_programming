#!/usr/bin/node

argCount = 0;
exports.logMe = function (item) {
  console.log(argCount + ': ' + item);
  argCount += 1;
}
