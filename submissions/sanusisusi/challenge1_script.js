const fs = require('fs');
const csv = require('csv-parser');

function loadSpotifyData(filePath) {
    // Load Spotify data from the CSV file
    return new Promise((resolve, reject) => {
        const data = [];
        fs.createReadStream(filePath)
            .pipe(csv())
            .on('data', (row) => {
                data.push(row);
            })
            .on('end', () => {
                resolve(data);
            })
            .on('error', (error) => {
                reject(error);
            });
    });
}

function countTotalSongs(data) {
    // Identify the number of songs in the file
    return data.length;
}

async function runChallenge() {
    // Adjust the filename and path as needed
    const filePath = 'spotify-2023.csv';

    // Load Spotify data
    const spotifyData = await loadSpotifyData(filePath);

    // Challenge 1: Identify the number of songs in the file
    const totalSongs = countTotalSongs(spotifyData);
    console.log(`Total number of songs: ${totalSongs}`);
}

runChallenge();
