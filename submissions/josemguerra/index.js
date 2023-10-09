const fs = require("fs");
const Papa = require("papaparse");

const spotify23Csv = fs.readFileSync("./spotify-2023.csv", "utf8");

const csv2Json = (csv) => {
  const results = Papa.parse(csv, {
    header: true,
    skipEmptyLines: true,
    dynamicTyping: true,
  });
  return results.data;
};

const data = csv2Json(spotify23Csv);

//results:
// Write a script to identify the number of songs in the file.
console.log(`Total number of songs: ${data.length}`);
// Write a script that identify the number of songs in the key of E.
let songsInKeyE = data.filter((song) => song.key === "E");
console.log(`Number of songs in the key of E: ${songsInKeyE.length}`);
// Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.
const mostCommonFieldToSearch = (fieldToSearch) => {
  let fieldCounts = {};
  data.forEach((song) => {
    let field = song[fieldToSearch];
    fieldCounts[field] = (fieldCounts[field] || 0) + 1;
  });

  let mostCommonField = Object.keys(fieldCounts).reduce((a, b) =>
    fieldCounts[a] > fieldCounts[b] ? a : b
  );
  console.log(
    `Most common ${fieldToSearch}: ${mostCommonField}, Occurrences: ${fieldCounts[mostCommonField]}`
  );
};

mostCommonFieldToSearch("artist(s)_name");
mostCommonFieldToSearch("released_year");
mostCommonFieldToSearch("released_month");
mostCommonFieldToSearch("released_day");
mostCommonFieldToSearch("key");
