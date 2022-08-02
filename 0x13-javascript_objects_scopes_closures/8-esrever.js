#!/usr/bin/node
exports.esrever = function (list) {
  let right = 0;
  let left = list.length - 1;
  let temp;
  while (right < left) {
    temp = list[left];
    list[left] = right;
    list[right] = temp;

    right += 1;
    left -= 1;
  }
  return list;
};
