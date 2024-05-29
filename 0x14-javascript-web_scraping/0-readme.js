#!/usr/bin/node

/**
 * This script reads and prints the content of a file.
 *
 * Usage: ./0-readme.js <file-path>
 *
 * The script takes one argument:
 * - The file path of the file to be read.
 *
 * It reads the file in UTF-8 encoding and prints its content to the console.
 * If an error occurs during the reading process, it prints the error object.
 */

const fs = require('fs'); // Import the file system module

// Get the file path from command line arguments
const filePath = process.argv[2];

// Check if the file path argument is provided
if (!filePath) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}

// Read the file in utf-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    // Print the error object if an error occurred
    console.error(err);
    return;
  }
  // Print the content of the file
  console.log(data);
});
