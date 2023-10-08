// Challenge 1:
//read CSV file into a string variable
const fs = require('fs');
const csvFile = fs.readFileSync('spotify-2023.csv', 'utf8');
//split the csv string into lines with the newline character
const lines = csvFile.split('\n');
//output the number of songs to the console, subtracting one line to account for the header
console.log(`Challenge 1 | The number of songs in this file: ${lines.length - 1}`);


//Challenge 2:
const keys = [];

//for each line of the csv, 
lines.forEach((line) => {
  //split the values into columns
  const columns = line.split(',');
  //assign the variable key to column 16
  const key = columns[16];
  //push the key of each column entry to initial keys array
  keys.push(key);
});
//create a new array containing only keys of 'E' with the filter method.
let E_keys = keys.filter(key => key === 'E');
//output the number of songs in the key of E to the console
console.log(`Challenge 2 | The number of songs in this file in the key of E: ${E_keys.length}`);


// Challenge 3
const rows = csvFile.split('\n');
// use reduce method to iterate over the rows of the file and the frequency of each value, contain the count of each value in an object.
const valueCounts = rows.reduce((prev, curr) => {
  const values = curr.split(',');
  const value = values[0]; //assuming the value is in the first column  
  prev[value] = (prev[value] || 0) + 1;
  return prev;
}, {});

const mostFrequentValue = Object.entries(valueCounts).reduce((prev, curr) => {
  if (curr[1] > prev[1]) {
    return curr;
  }
  return prev;
}, [null, 0]);

// output the most commonly occurring value of the file to the console
console.log(`Challenge 3 | The most commonly occurring value is ${mostFrequentValue[0]} with a frequency of ${mostFrequentValue[1]}`);