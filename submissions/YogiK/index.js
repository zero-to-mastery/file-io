const fs = require('fs');
const csv = require('csv-parser');
const csvParser = require('csv-parser');

const spotifyData = [];
const artistCount = {};

let totalSongs = 0;
let songsWithE = 0;

// Challenge 1 and 2
async function spotifyDataLogger() {
    return new Promise((resolve, reject) => {
        fs.createReadStream('./spotify-2023.csv')
            .pipe(csvParser())
            .on('data', (row) => {
                spotifyData.push(row);
            })
            .on('end', () => {
                resolve();
            })
            .on('error', (error) => {
                reject(error);
            });
    });
}

async function processData() {
    try {
        await spotifyDataLogger();

        const totalSongs = spotifyData.length;
        const songsWithE = spotifyData.filter(song => song.key === 'E').length;

        spotifyData.forEach(song => {
            const artist = song['artist(s)_name'];
            artistCount[artist] = (artistCount[artist] || 0) + 1;
        });

        const mostCommonArtist = Object.keys(artistCount).reduce((a, b) => {
            return artistCount[a] > artistCount[b] ? a : b;
        }, null);

        console.log(`Number of total songs: ${totalSongs}`);
        console.log(`Number of songs in the key of E: ${songsWithE}`);
        console.log(`Common artist: ${mostCommonArtist} (${artistCount[mostCommonArtist]} occurrences)`);
    } catch (error) {
        console.error('Error processing data:', error);
    }
}

processData();