#!/usr/bin/node
// This script writes a string to a file.

const fs = require('fs');

const filePath = process.argv[2];

const stringToWrite = process.argv[3];

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
