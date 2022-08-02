#!/usr/bin/node
exports.esrever = function (list) {
  let left = 0;
  let right = list.length - 1;
  let temp;
  while (left < right) {
    temp = list[left];
    list[left] = right;
    list[right] = temp;

    left += 1;
    right -= 1;
  }
  return list;
};
