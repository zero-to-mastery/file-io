const { parse } = require('csv-parse');
const fs = require('fs')

function parseCsv() {
    const test = fs.readFileSync("./spotify-2023.csv");

    let numberOfSongs = 0;
    let numberOfKeyOfESongs = 0;
    const artistNameMapping = {};

    const parser = parse(test, {
        delimiter: ',',
        columns: true,
    });

    parser.once('readable', () => {
        let record;
        while ((record = parser.read()) !== null) {
            numberOfSongs++;
            
            if (record.key === 'E') {
                numberOfKeyOfESongs++;
            }

            if (artistNameMapping[record['artist(s)_name']]) {
                artistNameMapping[record['artist(s)_name']]++;
            } else {
                artistNameMapping[record['artist(s)_name']] = 1;
            }
        }

        let commonArtistName = "";
        let commonArtistNameOccurence = 0;

        for (const key in artistNameMapping) {
            const val = artistNameMapping[key];
            if (val > commonArtistNameOccurence) {
                commonArtistName = key;
                commonArtistNameOccurence = val;
            }
        }

        console.log(`Number of songs: ${numberOfSongs}`);
        console.log(`Number of key of E songs: ${numberOfKeyOfESongs}`);
        console.log(`Most common artist name: ${commonArtistName}`);
    });

    parser.on('error', function (err) {
        console.error(err.message);
    });

}

parseCsv();