const fs = require("fs");
const { parse } = require("csv-parse");

const numberOfSongs = [];
const numberofSongsInE = [];
const columnValue = [];
const count = {};
let maxCount = -1;
let mostCommonValue = null;

fs.createReadStream("./spotify-2023.csv")
  .pipe(
    parse({
      delimiter: ",",
      columns: true,
    })
  )
  .on("data", (data) => {
    numberOfSongs.push(data);
    if (data["key"] === "E") numberofSongsInE.push(data);
  })
  .on("data", (row) => {
    let value = row["artist(s)_name"];
    if (value) columnValue.push(value);
  })
  .on("error", (err) => {
    console.log(err);
  })
  .on("end", () => {
    columnValue.forEach((d) => {
      !count[d] ? (count[d] = 1) : ++count[d];
      if (count[d] >= maxCount) {
        maxCount = count[d];
        mostCommonValue = d;
      }
    });
    console.log(`There are ${numberOfSongs.length} songs in the list.`);
    console.log(`There are ${numberofSongsInE.length} songs in the key of E`);
    console.log(
      `The most popular artist is ${mostCommonValue} with ${maxCount} songs.`
    );
  });
