#!/usr/bin/node
const axios = require('axios').default;
const reqUrl = process.argv[2];
let counter = 0;
axios.get(reqUrl)
  .then(function (response) {
    for (let i = 0; i < response.data.count; i++) {
      if (String(response.data.results[i].characters).includes('18')) {
        counter = counter + 1;
      }
    }
    console.log(counter);
  })
  .catch(function (error) {
    console.error(error);
  });
