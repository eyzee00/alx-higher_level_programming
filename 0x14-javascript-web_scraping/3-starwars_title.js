#!/usr/bin/node
const request = require('request');
let string = 'https://swapi-api.alx-tools.com/api/films/';
let url = string + process.argv[2];
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
