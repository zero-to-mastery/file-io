const fs = require('fs');
const csv = require('csv-parser');

const csvFilePath = 'spotify-2023.csv';

function countSongsInKeyE() {
  let keyECount = 0;

  fs.createReadStream(csvFilePath)
    .pipe(csv())
    .on('data', (row) => {
      // Check if the "key" column is "E"
      if (row.key === 'E') {
        keyECount++;
      }
    })
    .on('end', () => {
      console.log(`Number of songs in the key of E: ${keyECount}`);
    });
}

countSongsInKeyE();
