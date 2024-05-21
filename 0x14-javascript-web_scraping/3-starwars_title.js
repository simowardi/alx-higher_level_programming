#!/usr/bin/node
// This script fetches and prints the title of a Star Wars movie based on the episode number.

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  // Make a GET request to the Star Wars API.

  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body); // Parse the response body as JSON.

  console.log(movie.title); // Print the title of the movie.
});
