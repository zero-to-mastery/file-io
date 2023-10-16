const csv = require("csv-parser");
const { CONNREFUSED } = require("dns");
const fs = require("fs");
const results = [];

fs.createReadStream("../../spotify-2023.csv")
  .pipe(csv())
  .on("data", (data) => results.push(data))
  .on("end", () => {
    console.log("Number of songs in the file: ", results.length);
    console.log("Number of songs in the file that match the key 'E': ", results.filter((song) => song.key === "E").length);
    console.log("Occurences of the values in the given file: ");

    const store = {};
    const field = "released_year";
    let maxValue = -1;
    let frequentData = undefined;

    results
      .map((song) => song[field])
      .forEach((item) => {
        if (!store[item]) store[item] = 1;
        else store[item] += 1;

        if (store[item] > maxValue) {
          frequentData = { value: item, occurences: store[item] };
          maxValue = store[item];
        }
      });

    console.log(store);
    console.log("Most common value in the '" + field + "' field:", frequentData);
  });
