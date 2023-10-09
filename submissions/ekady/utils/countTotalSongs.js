const fs = require("fs");
const csv = require("csv-parser");

// Function to count the number of songs in the file
const countTotalSongs = (filePath) => {
  let totalSongs = 0;

  fs.createReadStream(filePath)
    .pipe(csv())
    .on("data", () => {
      totalSongs++;
    })
    .on("end", () => {
      console.log(`Total number of songs: ${totalSongs}`);
    });
};

module.exports = countTotalSongs;
