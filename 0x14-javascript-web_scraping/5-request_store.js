#!/usr/bin/node
const fs = require('fs');
const axios = require('axios').default;
const reqUrl = process.argv[2];
axios.get(reqUrl)
  .then(function (response) {
    fs.writeFile(process.argv[3], response.data, (err, data) => {
      if (err) {
        console.error(err);
      }
    });
  });
