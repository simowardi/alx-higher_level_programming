#!/usr/bin/node

/**
 * This script writes a string to a file.
 *
 * Usage: ./1-writeme.js <file-path> <string-to-write>
 *
 * The script takes two arguments:
 * - The file path where the string should be written.
 * - The string to write to the file.
 *
 * The content of the file is written in UTF-8 encoding.
 * If an error occurs during the writing process, it prints the error object.
 */

// Import the file system module
const fs = require('fs');

// Get the file path and string to write from command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Check if both arguments are provided
if (!filePath || !stringToWrite) {
  console.error('Usage: ./1-writeme.js <file-path> <string-to-write>');
  process.exit(1);
}

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    // Print the error object if an error occurred
    console.error(err);
    return;
  }
  console.log(`Successfully wrote to ${filePath}`);
});
