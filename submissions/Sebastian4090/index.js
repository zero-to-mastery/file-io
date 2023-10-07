const fs = require('fs');
const { parse } = require('csv-parse');

let songsArray = 0;
let songsArrayKeyE = 0;
const mostCommonYear = [];

// Read .csv file
fs.createReadStream("./spotify-2023.csv")
.pipe(parse({ delimiter: ",", from_line: 2 }))
.on("data", function(song) {
    if (song[15] === "E"){
        songsArrayKeyE++;
    }
    
    mostCommonYear.push(song[3]);
    songsArray++;
})
.on("end", function() {
    const objYear = {};
    let maxElement = mostCommonYear[0]
    let maxCount = 1;

    // Calculate most common year
    for (let i=0; i< mostCommonYear.length; i++) {
        let curr = mostCommonYear[i];

        if (!objYear[curr]) {
            objYear[curr] = 1;
        } else {
            objYear[curr] = objYear[curr] + 1;
        }

        if (objYear[curr] > maxCount) {
            maxElement = curr;
            maxCount = objYear[curr];
        }
    };
    
    console.log(`Number of songs in .csv file = ${songsArray}`);
    console.log(`Number of songs in the key E = ${songsArrayKeyE}`);
    console.log(`Most common released year = ${maxElement}. It appears ${maxCount} times.`);
})
.on("error", function (error) {
    console.log(error.message);
})