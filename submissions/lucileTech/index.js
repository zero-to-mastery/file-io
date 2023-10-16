const fs = require('fs');
const Papa = require('papaparse');

function readCSVFile(filePath) {
  try {
    const csvData = fs.readFileSync(filePath, 'utf8');
    return Papa.parse(csvData, { header: true, dynamicTyping: true });
  } catch (error) {
    console.error('Error reading or parsing CSV file:', error);
    return null;
  }
}

//Identify the number of songs in the file.

function countSongs(data) {
  return data ? data.data.length : 0;
}

//Identify the number of songs in the key of E.

function countSongsInKey(data, key) {
  return data ? data.data.filter(song => song.key === key).length : 0;
}

//Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.

function countOccurrences(data, columnName) {
  const valueCounts = {};
  if (data) {
    data.data.forEach(song => {
      const value = song[columnName];
      if (value) {
        valueCounts[value] = (valueCounts[value] || 0) + 1;
      }
    });
  }
  return valueCounts;
}

function findMostCommonValue(occurrences) {
  let mostCommonValue = null;
  let highestCount = 0;

  for (const value in occurrences) {
    if (occurrences[value] > highestCount) {
      mostCommonValue = value;
      highestCount = occurrences[value];
    }
  }

  return mostCommonValue;
}

const filePath = 'spotify-2023.csv';
const csvData = readCSVFile(filePath);

if (csvData) {
  console.log(`Number of songs in the CSV file: ${countSongs(csvData)}`);
  console.log(`Number of songs in the key of E: ${countSongsInKey(csvData, 'E')}`);

  const artistOccurrences = countOccurrences(csvData, 'artist(s)_name');
  const mostCommonArtist = findMostCommonValue(artistOccurrences);
  console.log(`Most common artist: ${mostCommonArtist}`);
}
