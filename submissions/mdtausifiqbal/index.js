const { parse } = require("csv-parse");
const fs = require("fs");

const filePath = "./spotify-2023.csv";
const columnToBeAnalyze = "artist(s)_name";

let totalSongs = 0;
let totalSongsInKeyOfE = 0;
let counting = new Map();

const parser = parse({
    columns: true,
});

fs.createReadStream(filePath)
    .pipe(parser)
    .on("error", (err) => {
        console.error(err);
    })
    .on("data", (row) => {
        totalSongs++;

        if (row["key"] === "E") totalSongsInKeyOfE++;

        let columnValue = row[columnToBeAnalyze];
        if (counting.has(columnValue)) {
            counting.set(columnValue, counting.get(columnValue) + 1);
        } else {
            counting.set(columnValue, 1);
        }
    })
    .on("end", function () {
        let countingArr = [...counting.entries()].sort((a, b) => b[1] - a[1]);
        console.log(`Total songs: ${totalSongs}`);
        console.log(`Total songs in key of E: ${totalSongsInKeyOfE}`);
        console.log(
            `Most common value in column ${columnToBeAnalyze} is ${countingArr[0][0]} with ${countingArr[0][1]} occurrences`
        );
    });
