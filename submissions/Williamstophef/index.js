//remember to chage the package.json file type to module to use ES6 import feature
//install fs and csv-parser
import fs from "fs";
import csv from "csv-parser";

//array to hold the datat as it is parsed through
const results = [];
//variable to count the number of songs in the csv
let songCount = 0;

//imports the CSV
fs.createReadStream("spotify-2023.csv")
  .pipe(csv())
  .on("data", (data) => {
    results.push(data);
    songCount++;
  })
  .on("end", () => {
    // console.log(results);
    console.log(`The number of songs in the Spotify 2023 list is ${songCount}`);
  });
