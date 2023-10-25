const fs = require('fs');

// Function to read the CSV file
//specifies the character encoding to be used when reading the file - 'utf8' because it's common for text files
function readCSVFile(filename) {
  return fs.readFileSync(filename, 'utf8');
}

// Function to count the number of songs
function countNumberOfSongs(csvFile) {
  const lines = csvFile.split('\n');
  console.log(`Challenge 1 | The number of songs in this file: ${lines.length - 1}`);
}

// Function to count the number of songs in the key of 'E' (key is a header in the 16 column)
function countSongsInKeyE(csvFile) {
    const keys = csvFile.split('\n').map(line => {
      const columns = line.split(',');
      return columns[16];
    });
    const E_keys = keys.filter(key => key === 'E');
    console.log(`Challenge 2 | The number of songs in the key of E: ${E_keys.length}`);
  }

// Function to find the most frequently occurring value
function findMostFrequentValue(csvFile) {
  const rows = csvFile.split('\n');
  const valueCounts = {};

  // Count the frequency of values in the first column
  rows.forEach(row => {
    const value = row.split(',')[0];
    valueCounts[value] = (valueCounts[value] || 0) + 1;
  });

  // Find the most frequent value
  const mostFrequentValue = Object.entries(valueCounts).reduce((prev, curr) => {
    return curr[1] > prev[1] ? curr : prev;
  }, [null, 0]);

  console.log(`Challenge 3 | The most commonly occurring value is ${mostFrequentValue[0]} with a frequency of ${mostFrequentValue[1]}`);
}

// EXTRA // Function to extract and print the headers
function extractHeaders(csvFile) {
    // Split the CSV file into lines
    const lines = csvFile.split('\n');
    console.log('Headers:', lines[0]);
  }


// Main part of the script

const filename = 'spotify-2023.csv';
const csvFile = readCSVFile(filename);

// Execute the three challenges
countNumberOfSongs(csvFile);
countSongsInKeyE(csvFile);
findMostFrequentValue(csvFile);

// Call the function to extract and print the headers
extractHeaders(csvFile);