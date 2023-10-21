const fs = require('fs');
const papa = require('papaparse');

// Function to count songs with a specific key
function countSongsWithKey(data, key) {
  return data.filter(song => song.key === key).length;
}

// Function to count occurrences of values in a specified column
function countOccurrencesOfValues(data, columnName) {
  const artistCounts = new Map();

  data.forEach(row => {
    const artists = row[columnName].split(', ');
    artists.forEach(artist => {
      artistCounts.set(artist, (artistCounts.get(artist) || 0) + 1);
    });
  });

  let mostCommonArtist = null;
  let maxCount = 0;

  artistCounts.forEach((count, artist) => {
    if (count > maxCount) {
      maxCount = count;
      mostCommonArtist = artist;
    }
  });

  return mostCommonArtist;
}

// Read the CSV file
const csvFilePath = 'spotify-2023.csv';
const csvData = fs.readFileSync(csvFilePath, 'utf8');

papa.parse(csvData, {
  header: true,
  skipEmptyLines: true,
  complete: function(results) {
    // Solution 1: Number of songs
    const numOfSongs = results.data.length;
    console.log('Number of songs:', numOfSongs);

    // Solution 2: Number of songs with key 'E'
    const numOfSongsWithE = countSongsWithKey(results.data, 'E');
    console.log('Number of songs with key E:', numOfSongsWithE);

    // Solution 3: Most streamed artist
    const mostStreamedArtist = countOccurrencesOfValues(results.data, 'artist(s)_name');
    console.log('Most streamed artist:', mostStreamedArtist);
  },
});
