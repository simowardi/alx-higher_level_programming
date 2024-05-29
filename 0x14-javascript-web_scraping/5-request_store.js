#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file

const apiUrl = process.argv[2];

const stringToWrite = process.argv[3];

// Import the built-in Node.js 'fs' module
const fs = require('fs');

const request = require('request');

// Use the 'request' module to perform an HTTP GET request to the URL
request(apiUrl).pipe(fs.createWriteStream(stringToWrite));
