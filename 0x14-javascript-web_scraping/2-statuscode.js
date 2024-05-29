#!/usr/bin/node

// This script makes a request to the received URL and displays the status code.

const request = require('request');

request.get(process.argv[2]).on('response', function (response) {
  // Use the 'request' module to perform an HTTP GET request to the URL.
  // Set up an event listener for the 'response' event emitted by the HTTP request.

  console.log(`code: ${response.statusCode}`);
  // Log the HTTP status code of the response to the console.
});
