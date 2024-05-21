#!/usr/bin/node
// This script writes a string to a file.
// Import the file system module

const fs = require('fs');

// Get the file path and string to write from command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf8', (error) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(`Successfully wrote to ${filePath}`);
});
