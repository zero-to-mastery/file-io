const fs = require('fs');
const csvParser = require('csv-parser');

let count = 0;  // variable to count total number of songs in the file
let keyCount = 0; // variable to count total number of songs having 'E' as a key


//Write a script to identify the number of songs in the file.
const songsCount = (data) => {
    count++;
}

// Write a script that identify the number of songs in the key of E.
const findKey = (data) => { 

    if(data['key'] == 'E'){
        keyCount++;
    }
}


fs.createReadStream('spotify-2023.csv').pipe(csvParser())
.on('data' , (row) => {
    songsCount(row);
    findKey(row);
})
.on('end' , () => {
    console.log('completed');
    console.log('Total number of songs in the file = ' , count);
    console.log('Total number of songs with key E = ' , keyCount);
})

