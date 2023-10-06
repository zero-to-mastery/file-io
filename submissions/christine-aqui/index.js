const fs = require("fs");
const csvParser = require("csv-parser");
const { finished } = require("stream/promises");

const file = "spotify-2023.csv";

let totalSongs = 0;
let songsInKeyOfE = 0;
let artistCounts = {};

async function processCSV() {
  const stream = fs
    .createReadStream(file)
    .pipe(csvParser())
    .on("data", (row) => {
      totalSongs++;

      if (row.key === "E") {
        songsInKeyOfE++;
      }

      let artist = row["artist(s)_name"];
      artistCounts[artist] = (artistCounts[artist] || 0) + 1;
    });

  await finished(stream);

  console.log("Total songs in the file:", totalSongs);
  console.log("Total songs in the key of E:", songsInKeyOfE);

  let mostCommonArtist = Object.keys(artistCounts).reduce((a, b) =>
    artistCounts[a] > artistCounts[b] ? a : b
  );

  console.log(
    "Most common artist:",
    mostCommonArtist,
    "with",
    artistCounts[mostCommonArtist],
    "songs"
  );
}

processCSV().catch((error) => {
  console.log("Error processing the file:", error);
});
