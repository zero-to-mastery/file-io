const fs = require('fs');
const parser = require('csv-parser'); // https://www.npmjs.com/package/csv-parser

const csvFilePath = './spotify-2023.csv'; // path to your Spotify CSV file


/** Function to count total songs in the given csv file**/
function countTotalSongs() {
    let totalSongs = 0;
  
    fs.createReadStream(csvFilePath)
      .pipe(parser())
      .on('data', () => {
        totalSongs++;
      })
      .on('end', () => {
        console.log(`Total number of songs in the file: ${totalSongs}`);
      });
  }
/**Function to identify number of Songs in Key 'E' */
function countSongsInKeyE() {
  let songsInKeyE = 0;

  fs.createReadStream(csvFilePath)
    .pipe(parser())
    .on('data', (row) => {
      if (row.key === 'E') {
        songsInKeyE++;
      }
    })
    .on('end', () => {
      console.log(`Number of songs in the key of E: ${songsInKeyE}`);
    });
}

/**Function to count occurances and find the most common value */
function countOccurrencesAndFindMostCommon(columnName) {
  const occurrences = {};
  let mostCommonValue = '';
  let maxCount = 0;

  fs.createReadStream(csvFilePath)
    .pipe(parser())
    .on('data', (row) => {
      const columnValue = row[columnName];
      if (columnValue) {
        if (occurrences[columnValue]) {
          occurrences[columnValue]++;
        } else {
          occurrences[columnValue] = 1;
        }

        if (occurrences[columnValue] > maxCount) {
          maxCount = occurrences[columnValue];
          mostCommonValue = columnValue;
        }
      }
    })
    .on('end', () => {
      console.log(`Most common value in column '${columnName}': ${mostCommonValue}`);
      console.log(`Number of occurrences of the most common value: ${maxCount}`);
    });
}



// Print the Following
countTotalSongs();
countSongsInKeyE();
countOccurrencesAndFindMostCommon('artist(s)_name');
