const { parse: parseCsv } = require('csv-parse');
const fs = require('fs');

//  empty array to store the song data.
const songsData = [];

//  empty array to store the songs in the key of E.
const songsInKeyE = [];

//  empty object to store the artist counts.
const artistCounts = {};

// The column that we will be analyzing.
const columnToAnalyze = 'artist(s)_name';

// function to check if a song is in the key of E.
function isKeyE(song) {
  return song['key'] === 'E';
}

// Read the CSV file and parse it into an array of objects.
fs.createReadStream('spotify-2023.csv')
  .pipe(parseCsv({
    columns: true
  }))
  // Iterate over the array of song objects.
  .on('data', (row) => {
    // Add the song object to the songsData array.
    songsData.push(row);

    // If the song is in the key of E, add it to the songsInKeyE array.
    if (isKeyE(row)) {
      songsInKeyE.push(row);
    }

    // Get the artists for the song.
    const artists = row[columnToAnalyze].split(', ');

    // Only count the song if there is exactly one artist.
    if (artists.length === 1) {
      // Get the artist name.
      const artist = artists[0];

      // Increment the count for the artist.
      artistCounts[artist] = (artistCounts[artist] || 0) + 1;
    }
  })
  // Handle any errors that occur while reading the CSV file.
  .on('error', (err) => {
    console.log(`Error reading CSV: ${err}`);
  })
  // Once all of the data has been read, print the results to the console.
  .on('end', () => {
    // Get the total number of songs in the dataset.
    const totalSongs = songsData.length;

    // Get the number of songs in the key of E.
    const songsInECount = songsInKeyE.length;

    // Find the most popular individual artist.
    let mostPopularArtist = null;
    let maxCount = 0;

    for (const artist of Object.keys(artistCounts)) {
      const count = artistCounts[artist];
      if (count > maxCount) {
        mostPopularArtist = artist;
        maxCount = count;
      }
    }

    // Print the results to the console.
    console.log(`Total songs in the dataset: ${totalSongs}`);
    console.log(`Songs in the key of E: ${songsInECount}`);
    console.log(`The most popular individual artist is ${mostPopularArtist} with ${maxCount} songs.`);
  });