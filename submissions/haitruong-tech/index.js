const csv = require("csv-parser");
const fs = require("fs");

const col = process.argv[2]; // col to count the occurrences

/**
 * Cache holds occurences count
 * @type {{ [col_value]: count }}
 */
const occurences = {
  /**
   * E.g.
   * "Latto, Jung Kook": 23,
   */
};
let mostOccurrences = {
  value: "",
  count: 0,
};
let noOfSongs = 0;
let songsWithKeyE = 0;

fs.createReadStream("../../spotify-2023.csv")
  .pipe(csv())
  .on("data", (song) => {
    noOfSongs++;
    if (song.key === "E") songsWithKeyE++;
    if (col == null || song[col] == null) return;

    // As `artist(s)_name` column may holds multiple artists,
    // we need to split this column into multiple values
    const colValues = song[col].split(", ");
    colValues.forEach((value) => {
      occurences[value] ??= 0;
      occurences[value]++;
      if (occurences[value] > mostOccurrences.count) {
        mostOccurrences.value = value;
        mostOccurrences.count = occurences[value];
      }
    });
  })
  .on("end", () => {
    console.log("Total songs in the file:", noOfSongs);
    console.log("Total songs in the file with key 'E':", songsWithKeyE);
    if (col != null) console.log("Most common value:", mostOccurrences.value);
  });
