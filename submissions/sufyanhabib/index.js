const fs = require("fs");
const Papa = require("papaparse");
const inputFilePath = "./spotify-2023.csv";
const fileData = fs.readFileSync(inputFilePath, "utf8");
const csvData = Papa.parse(fileData, { header: true, dynamicTyping: true });

const songs = csvData.data;
const songsInTheKeyOfE = songs.filter((song) => song.key === "E");
const dayCounts = {};

songs.forEach((song) => {
  const year = song.released_year;
  const month = song.released_month;
  const day = song.released_day;
  const date = new Date(year, month - 1, day); // Month is 0-indexed
  const dayOfWeek = date.toLocaleString("en-US", { weekday: "long" });
  
  if (!dayCounts[dayOfWeek]) {
    dayCounts[dayOfWeek] = 0;
  }
  dayCounts[dayOfWeek]++;
});

const mostCommonDay = Object.keys(dayCounts).reduce((a, b) =>
  dayCounts[a] > dayCounts[b] ? a : b
);

console.log(`Total number of songs: ${songs.length}`);
console.log(`Number of songs in the key of 'E': ${songsInTheKeyOfE.length}`);
console.log(`The most common day to release songs is: ${mostCommonDay}`);
console.log(`Number of songs released on ${mostCommonDay}: ${dayCounts[mostCommonDay]}`);
