const fs = require("fs");
const csv = require("csv-parser");
const inputFilePath = "./spotify-2023.csv";
const songs = [];
const songsInTheKeyOfE = [];
const releasedDays = [];
const counts = {};
let mostCommonValue = null;
let maxCount = 0;

// The function returns true if the "key" property of the song object is equal to "E"
const keyOfE = (song) => song["key"] === "E";
const dayOfWeek = (year, month, day) => {
  const releasedDate = new Date(`${year}-${month}-${day}`);
  const dayNames = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];
  const dayName = releasedDate.getDay();
  return dayNames[dayName];
};

fs.createReadStream(inputFilePath)
  .pipe(csv())
  .on("data", (data) => {
    songs.push(data);
    releasedDays.push(
      dayOfWeek(data.released_year, data.released_month, data.released_day),
    );
    if (keyOfE(data)) {
      songsInTheKeyOfE.push(data);
    }
  })
  .on("end", () => {
    releasedDays.forEach((day) => {
      !counts[day] ? (counts[day] = 1) : counts[day]++;

      if (counts[day] > maxCount) {
        mostCommonValue = day;
        maxCount = counts[day];
      }
    });

    console.log(`There are ${songs.length} songs in this list.`);
    console.log(
      `There are ${songsInTheKeyOfE.length} songs in the key of 'E'.`,
    );
    console.log(
      `The most popular day of the week to release a song is on a ${mostCommonValue} with ${maxCount} songs released.`,
    );
  });
