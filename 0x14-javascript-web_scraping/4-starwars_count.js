#!/usr/bin/node
const axios = require('axios').default;
const reqUrl = process.argv[2];
const dict = {};
let i = 0;
axios.get(reqUrl)
  .then(function (response) {
    for (i = 0; i < response.data.length; i++) {
      if (!dict[response.data[i].userId]) {
        dict[response.data[i].userId] = 0;
      }
      if (response.data[i].completed === true) {
        dict[response.data[i].userId] += 1;
      }
    }
    console.log(map);
  });
