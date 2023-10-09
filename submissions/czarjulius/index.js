const path = require('path');
const spotifyDataAnalyzer = require('./spotifyDataAnalyzer');

const csvFilePath = path.join(__dirname, 'spotify-2023.csv');

const key = 'E';
const columnToCount = 'artist(s)_name';

spotifyDataAnalyzer(csvFilePath, { key, columnToCount })
  .then((result) => {
    console.log(`Total number of songs in the CSV file: ${result.totalSongs}`);
    console.log(`Total number of songs in the key of E: ${result.keyESongs}`);
    console.log(
      `Most common value in the "artist(s)_name" column: ${result.mostCommonValue} (${result.highestCount} occurrences)`
    );
  })
  .catch((error) => {
    console.error('Error:', error.message);
  });
