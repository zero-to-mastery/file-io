const csv = require("csv-parser");
const fs = require("fs");

let noOfSongs = 0;
let songsWithKeyE = 0;

fs.createReadStream("../../spotify-2023.csv")
  .pipe(csv())
  .on("data", (song) => {
    noOfSongs++;
    if (song.key === "E") songsWithKeyE++;
  })
  .on("end", () => {
    console.log("Total songs in the file:", noOfSongs);
    console.log("Total songs in the file with key 'E':", songsWithKeyE);
  });
