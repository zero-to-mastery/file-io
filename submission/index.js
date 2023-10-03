const { parse } = require('csv-parse');
const fs = require('fs');
const path = require('path');

let appleArtist = [];
let getAllKeyOfESongs = [];

//find popular artist
let analyzeColumn = 'artist(s)_name';
const values = [];

const keyOfE = (artist) => {
  return artist['key'] === 'E';
};

function findPopularArtist() {
  return new Promise((resolve, reject) => {
    fs.createReadStream(path.join(__dirname, 'data', 'spotify-2023.csv'))
      .pipe(parse({ columns: true }))

      .on('data', async (data) => {
        appleArtist.push(data);

        if (keyOfE(data)) {
          getAllKeyOfESongs.push(data);
        }
      })

      .on('data', async (row) => {
        const newValues = row[analyzeColumn];
        if (newValues) {
          values.push(newValues);
        }
      })

      .on('err', (err) => {
        console.log(err);
        reject(err);
      });
  });
}

console.log(`there are ${appleArtist.length} in this list`);
