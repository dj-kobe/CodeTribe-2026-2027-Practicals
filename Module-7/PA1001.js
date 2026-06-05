//Number processor
//printing out even numbers from an array of numbers from 1 to 70, with some duplicates

var i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

//function printEvenNumbers(arr) {
//for (var i = 0; i < arr.length; i++) {
//   if (arr[i] % 2 === 0) {
//     console.log(arr[i]);
//   }
// }
//}

//printEvenNumbers(i);

for (let i = 1; i <= 10; i++) {
  if (i === 3 || i === 6) {
    continue;
  }
  console.log(i);
}

var j = [1, 3, 43, 4, 5, 6, 1653, 8, 10, 111];

function bubbleSort(arr) {
  let len = arr.length;

  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
}

console.log(bubbleSort(j));
