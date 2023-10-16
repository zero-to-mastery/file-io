import * as fs from 'fs';
import csvParser from 'csv-parser';

const csvFilePath = '../../../spotify-2023.csv';

// Task 1: Identify the number of songs in the file
function countSongs() {
  let count: number = 0;
  fs.createReadStream(csvFilePath)
    .pipe(csvParser())
    .on('data', () => count++)
    .on('end', () => console.log(`Number of songs: ${count}`));
}

// Task 2: Identify the number of songs in the key of E
function countSongsInKeyE() {
  let count: number = 0;
  fs.createReadStream(csvFilePath)
    .pipe(csvParser())
    .on('data', (row: { key: string }) => {
      if (row['key'] === 'E') {
        count++;
      }
    })
    .on('end', () => console.log(`Number of songs in the key of E: ${count}`));
}

// Task 3: Count occurrences of values in a specified column (artist(s)_name)
function mostCommonArtist(filePath: string) {
  const artistCounts = new Map<string, number>();

  fs.createReadStream(csvFilePath)
    .pipe(csvParser())
    .on('data', (row: { 'artist(s)_name': string }) => {
      const artistName = row['artist(s)_name'];

      if (artistCounts.has(artistName)) {
        artistCounts.set(artistName, artistCounts.get(artistName)! + 1);
      } else {
        artistCounts.set(artistName, 1);
      }
    })
    .on('end', () => {
      let mostPopularArtist = '';
      let maxCount = 0;

      artistCounts.forEach((count, artist) => {
        if (count > maxCount) {
          mostPopularArtist = artist;
          maxCount = count;
        }
      });

      if (mostPopularArtist) {
        console.log(`The most popular artist is ${mostPopularArtist} with ${maxCount} songs.`);
      } else {
        console.log('No artist data found.');
      }
    })
    .on('error', (error) => {
      console.error('Error reading the CSV file:', error);
    });
}

// Run the tasks
countSongs();
countSongsInKeyE();
mostCommonArtist(csvFilePath);
