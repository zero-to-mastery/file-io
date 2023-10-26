const csv = require('csv-parser')
const fs = require('fs')
const results = [];

fs.createReadStream('../../spotify-2023.csv')
    .pipe(csv())
    .on('data', (data) => results.push(data))
    .on('end', () => {
        const numberOfSongs = results.length;
        const withEKeys = results.reduce((acc, current)=>{
            if (current.key === 'E') acc++;
            return acc;
        }, 0)
        const artistsOccurrences = {};
        let mostCommonArtist = '';
        let highestOccurrence = 0;
        results.forEach((item)=>{
            let currentKey = item['artist(s)_name'];
            if (artistsOccurrences.hasOwnProperty(currentKey)){
                let currentNumber = ++artistsOccurrences[currentKey];
                if (currentNumber > highestOccurrence){
                    mostCommonArtist = currentKey;
                    highestOccurrence = currentNumber
                }
            }
            else {
                artistsOccurrences[currentKey] = 1;
            }
        });
        console.log({
            numberOfSongs,
            withEKeys,
            mostCommonArtist
        })
    });
