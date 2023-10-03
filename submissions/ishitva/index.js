const { parse: parseCsv } = require('csv-parse');
const fs = require('fs');

const songsData = [];
const songsInKeyE = [];
const artistCounts = {};

const columnToAnalyze = 'artist(s)_name';

function isKeyE(song) {
  return song['key'] === 'E';
}

fs.createReadStream('spotify-2023.csv')
  .pipe(parseCsv({
    columns: true
  }))
  .on('data', (row) => {
    songsData.push(row);

    if (isKeyE(row)) {
      songsInKeyE.push(row);
    }

    const artists = row[columnToAnalyze].split(', ');
    // Only count the song if there is exactly one artist.
    if (artists.length === 1) {
      const artist = artists[0];
      artistCounts[artist] = (artistCounts[artist] || 0) + 1;
    }
  })
  .on('error', (err) => {
    console.log(`Error reading CSV: ${err}`);
  })
  .on('end', () => {
    const totalSongs = songsData.length;
    const songsInECount = songsInKeyE.length;

    let mostPopularArtist = null;
    let maxCount = 0;

    Object.keys(artistCounts).forEach((artist) => {
      if (artistCounts[artist] > maxCount) {
        mostPopularArtist = artist;
        maxCount = artistCounts[artist];
      }
    });

    console.log(`Total songs in the dataset: ${totalSongs}`);
    console.log(`Songs in the key of E: ${songsInECount}`);
    console.log(`The most popular individual artist is ${mostPopularArtist} with ${maxCount} songs.`);
  });
