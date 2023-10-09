const csv = require("csv-parse");
const fs = require("fs");

const songs = [];
const authors = {};

async function readCsvFile() {
  fs.createReadStream("./spotify-2023.csv")
    .pipe(csv.parse({ delimiter: ",", from_line: 2 }))
    .on("data", (songChunk) => {
      songs.push(songChunk);

      if (authors[songChunk[1]] !== undefined)
        authors[songChunk[1]] = authors[songChunk[1]] + 1;
      else authors[songChunk[1]] = 1;
    })
    .on("error", function (error) {
      console.log(error.message);
    })
    .on("end", () => {
      // number of songs startig with E or e
      const songsWithE = findSongsWithE();
      // returns the author who has max songs
      const { maxAuthor, maxSongs } = findAuthorWithMostSongs();

      console.log(`total number of songs: ${songs.length}`);
      console.log(
        `The author with the most songs is ${maxAuthor} with ${maxSongs} songs.`
      );
      console.table(songsWithE);
    });
}

function findSongsWithE() {
  const songsWithE = [];
  songs.forEach((song) => {
    if (song[0].startsWith("E") || song[0].startsWith("e")) {
      songsWithE.push(song[0]);
    }
  });

  return songsWithE;
}

function findAuthorWithMostSongs() {
  let maxAuthor = "";

  // starting max as -1
  let maxSongs = -1;

  // authors with most songs
  for (const author in authors) {
    // checking if the current author has max songs
    if (authors[author] > maxSongs) {
      maxAuthor = author;
      maxSongs = authors[author];
    }
  }

  return {
    maxSongs,
    maxAuthor,
  };
}

readCsvFile();
