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

console.log(`There are ${songs.length} songs in this list.`);
console.log(`There are ${songsInTheKeyOfE.length} songs in the key of 'E'.`);
console.log(
  `The most popular day of the week to release a song is on a ${mostCommonDay} with ${dayCounts[mostCommonDay]} songs released.`
);
