#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file


// Import the built-in Node.js 'fs' module
const fs = require('fs');

// Import the 'request' module
const request = require('request');

const apiUrl = process.argv[2];

// Use the 'request' module to perform an HTTP GET request to the URL
request(apiUrl).pipe(fs.createWriteStream(process.argv[3]));
