#!/usr/bin/node
/* Script that writes a string to a file
*/

const fs = require('fs');
const filename = process.argv[2];
const contents = process.argv[3];
fs.writeFile(filename, contents, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
