import csv from 'csv-parser';
import fs from 'fs';

const result = [];

fs.createReadStream('../../spotify-2023.csv')
    .pipe(csv())
    .on('data', (data) => result.push(data))
    .on('end', () => {
        console.log('The number of songs in the file:',result.length);

        const songsStartingWithE = result.filter( item => item.key.startsWith('E'));

        console.log('The number of songs in the key of E:', songsStartingWithE.length);

        const artistCount = {};

        result.forEach(item => {
            const artistNames = item['artist(s)_name'].split(', ');
               
            artistNames.forEach((artist)=>{
                if (artistCount[artist]) {
                    artistCount[artist]++;
                }
                else {
                    artistCount[artist] = 1;
                }
            });
           });

           let mostCommonArtist = '';
           let mostCommonCount = 0;

        for( const artist in artistCount ){
            if(artistCount[artist] > mostCommonCount ){
                mostCommonArtist = artist;
                mostCommonCount = artistCount[artist];
            }
        }

        console.log(`The most popular artist is ${mostCommonArtist} with ${mostCommonCount} songs.`);
    });