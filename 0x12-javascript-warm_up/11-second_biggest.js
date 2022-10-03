#!/usr/bin/node
const argv = process.argv;

function convertInt (arr) {
  const newArr = [];
  for (let i = 0; i < arr.length; i++) {
    newArr.push(parseInt(arr[i]));
  }
  return (newArr);
}
function findSecondBiggest (arr) {
  const a = arr.slice(2);
  if (a.length === 0 || a.length === 1) {
    return (0);
  }
  const intArray = convertInt(a);
  let result;
  const max = Math.max(...intArray);
  result = intArray[0];
  for (let i = 0; i < intArray.length; i++) {
    if (intArray[i] > result && intArray[i] < max) {
      result = intArray[i];
    }
  }
  return (result);
}

console.log(findSecondBiggest(argv));
