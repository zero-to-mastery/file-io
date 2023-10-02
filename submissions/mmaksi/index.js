const fs = require("fs");
const csv = require("csv-parser");
const path = require("path");

const findKeyWithHighestValue = require("./utils/csv");

const results = [];
let filteredResultsNum = 0;
const distinctArtistNames = {};

async function numOfArtistsInKey(key) {
  fs.createReadStream(path.join("..", "..", "spotify-2023.csv"))
    .pipe(csv())
    .on("data", (data) => {
      // Each row of data is processed here
      results.push(data);

      if (data["key"] === key) {
        filteredResultsNum++;
      }

      const artist = data["artist(s)_name"];

      if (!distinctArtistNames[artist]) {
        distinctArtistNames[artist] = 1;
      } else {
        distinctArtistNames[artist] += 1;
      }
    })
    .on("end", () => {
      // All data has been processed
      // Number of songs
      console.log(`Number of total songs: ${results.length}`);
      console.log(`Num of filtered songs: ${filteredResultsNum}`);
      //   console.log(`Distinct: ${distinctArtistNames}`);
      const highestValue = findKeyWithHighestValue(distinctArtistNames);
      console.log(
        `Highest value: ${highestValue}: ${distinctArtistNames[highestValue]}`,
      );
    });
}
numOfArtistsInKey("E");
