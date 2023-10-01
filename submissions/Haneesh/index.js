const fs = require("fs");
const parse = require("csv-parse").parse;

const csvPath = "../../spotify-2023.csv"; // I used the one in the GitHub Repo

const songs = [];
const authors = {};

fs.createReadStream(csvPath);

fs.createReadStream(csvPath)

    .pipe(parse({ delimiter: ",", from_line: 2 }))

    .on("data", function (row) {
        songs.push(row);
        if(authors[row[1]] !== undefined)
            authors[row[1]] = authors[row[1]] + 1;
        else
            authors[row[1]] = 1;
    })

    .on("error", function (error) {
        console.log(error.message);
    })

    .on("end", function () {
        console.log("finished");

        const temp = [];

        songs.forEach(song => {
            if(song[1].startsWith("E") || song[1].startsWith("e"))
                temp.push(song);
        });

        console.log("Number of Songs: " + songs.length);
        console.log("Number of Songs starting with E: " + temp.length);

        let maxAuthor = "";
        let maxSongs = -1;

        for (const author in authors) {
            if(authors[author] > maxSongs) {
                maxAuthor = author;
                maxSongs = authors[author];
            }
        }

        console.log(`The author with the most songs is ${maxAuthor} with ${maxSongs} songs.`);
    });
