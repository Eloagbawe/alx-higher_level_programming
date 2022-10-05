#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

const content = fs.readFileSync(argv[2], 'utf-8');
const content2 = fs.readFileSync(argv[3], 'utf-8');
const fullContent = content + '\n' + content2;
fs.appendFile(argv[4], fullContent, (err) => {
  if (err) throw err;
});
