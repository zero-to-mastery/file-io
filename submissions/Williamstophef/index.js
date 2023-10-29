//remember to change the package.json file type to module to use ES6 import feature
//install fs and csv-parser
import fs from "fs";
import csv from "csv-parser";

//array to hold the dataset as it is parsed through
const results = [];
//variable to count the number of songs in the csv
let songCount = 0;

//imports the CSV into the read stream
fs.createReadStream("spotify-2023.csv")
  //pipe is required for csv to process input to an output
  .pipe(csv())
  //event listener for data. Then passes in the data to a function to push it into the results array
  //Also increase the increment of the songCount
  .on("data", (data) => {
    //pushes each new entry of the object into an array
    results.push(data);
    songCount++;
  })
  //Triggered when the end of the readable stream is reached
  .on("end", () => {
    // console.log(results);
    console.log(
      `The number of songs in the Spotify 2023 playlist is ${songCount}`
    );
  });
