const fs = require('fs');
const csv = require('csv-parser');

const csvFilePath = 'spotify-2023.csv';

function analyzeSpotifyData() {
  const songsInKeyE = [];

  fs.createReadStream(csvFilePath)
    .pipe(csv())
    .on('data', (row) => {
      if (row.key === 'E') {
        songsInKeyE.push(row);
      }
    })
    .on('end', () => {
      console.log(`Number of songs in the key of E: ${songsInKeyE.length}`);
    });
}

analyzeSpotifyData();
