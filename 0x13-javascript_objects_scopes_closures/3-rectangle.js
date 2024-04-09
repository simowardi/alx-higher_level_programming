#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is 0 or not a positive integer, create an empty object
      this.width = 0;
      this.height = 0;
    }
  }

  // Instance method to print the rectangle using the character X
  print() {
    if (this.width === 0 || this.height === 0) {
      // If the rectangle is empty, do not print anything
      return;
    }
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;

