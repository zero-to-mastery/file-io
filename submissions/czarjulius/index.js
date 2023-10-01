const path = require('path');
const spotifyDataAnalyzer = require('./spotifyDataAnalyzer');

const csvFilePath = path.join(__dirname, 'spotify-2023.csv');

spotifyDataAnalyzer(csvFilePath)
  .then((result) => {
    console.log(`Total number of songs in the CSV file: ${result.totalSongs}`);
  })
  .catch((error) => {
    console.error('Error:', error.message);
  });
