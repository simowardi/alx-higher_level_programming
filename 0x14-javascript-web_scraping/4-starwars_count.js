#!/usr/bin/node
// This script prints the number of movies where the character "Wedge Antilles" (character ID 18) is present.

const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request(apiUrl, (error, response, body) => {
  // Make a GET request to the Star Wars API.

  if (error) {
    // Print the error object if an error occurred.
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;

  // Filter films where Wedge Antilles (character ID 18) is present
  const count = films.filter(film => film.characters.includes(`${apiUrl}${characterId}/`)).length;

  console.log(count)
});
