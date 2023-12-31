const fs = require('fs');
const csv = require('csv-parser');

// Specify the path to the CSV file
const csvFilePath = 'C:\\Users\\Manug\\OneDrive\\Área de Trabalho\\file-io\\file-io\\spotify-2023.csv';

// Function to read and process the CSV file
function analyzeSpotifyData() {
  const songsInKeyE = [];

  fs.createReadStream(csvFilePath)
    .pipe(csv())
    .on('data', (row) => {
      // Assuming the key column is named "key" in the CSV file
      if (row.key === 'E') {
        songsInKeyE.push(row);
      }
    })
    .on('end', () => {
      console.log(`Number of songs in the key of E: ${songsInKeyE.length}`);
    });
}

// Run the data analysis
analyzeSpotifyData();
