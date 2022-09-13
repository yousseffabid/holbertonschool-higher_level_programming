#!/usr/bin/node
const axios = require('axios').default;
const id = process.argv[2];
const reqUrl = `https://swapi-api.hbtn.io/api/films/${id}`;
axios.get(reqUrl)
  .then(function (response) {
    console.log('%s', response.data.title);
  });
