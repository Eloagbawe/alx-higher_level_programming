#!/usr/bin/node
const argv = process.argv;
let arr = argv.slice(2);

function convertInt (arr) {
  const newArr = [];
  for (let i = 0; i < arr.length; i++) {
    newArr.push(parseInt(arr[i]));
  }
  return (newArr);
}
function findSecondBiggest (a) {
  if (a.length === 0 || a.length === 1) {
    return (0);
  }
  arr = convertInt(a);
  arr.sort();
  return (arr[arr.length - 2]);
}

console.log(findSecondBiggest(arr));
