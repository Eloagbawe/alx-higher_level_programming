#!/usr/bin/node
const argv = process.argv;
const request = require('request');

request(argv[2], function (err, res, body) {
  if (err) throw err;
  const data = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < data.length; i++) {
    if (data[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
