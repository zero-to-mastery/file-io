const fs = require("fs");
const csv = require("csv-parser");

// Function to count the number of songs in the key
const countSongsInKey = (filePath, key = "E") => {
  let songsInKeyE = 0;

  fs.createReadStream(filePath)
    .pipe(csv())
    .on("data", (row) => {
      if (row.key === key) {
        songsInKeyE++;
      }
    })
    .on("end", () => {
      console.log(`Number of songs in the key of E: ${songsInKeyE}`);
    });
};

module.exports = countSongsInKey;
