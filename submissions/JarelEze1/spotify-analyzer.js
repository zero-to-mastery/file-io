const fs = require('fs');
const csv = require('csv-parser');

const csvFilePath = 'spotify-2023.csv';

function countSongs() {
  let songCount = 0;

  fs.createReadStream(csvFilePath)
    .pipe(csv())
    .on('data', (row) => {
      // For each row in the CSV, increment the song count
      songCount++;
    })
    .on('end', () => {
      console.log(`Total number of songs in the file: ${songCount}`);
    });
}

countSongs();

