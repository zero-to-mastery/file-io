
const fs = require('fs');
const Papa = require('papaparse');


const csvFile = fs.readFileSync('./spotify-2023.csv', 'utf8');


Papa.parse(csvFile, {
    header: true,
    dynamicTyping: true,
    complete: function (results) {
        const data = results.data;
        console.log('Total songs:', countSongs(data));
        console.log('Songs in key E:', countSongsInKeyE(data));

        const artistOccurrences = countOccurrences(data, 'artist');
        console.log('Most common artist:', findMostCommonValue(artistOccurrences));
    }
});

function countSongs(data) {
    return data.length;
}

function countSongsInKeyE(data) {
    return data.filter(row => row.key === 'E').length;
}

function countOccurrences(data, column) {
    const occurrences = {};
    data.forEach(row => {
        const value = row[column];
        occurrences[value] = (occurrences[value] || 0) + 1;
    });
    return occurrences;
}

function findMostCommonValue(occurrences) {
    let maxCount = 0;
    let mostCommonValue = null;
    for (const [value, count] of Object.entries(occurrences)) {
        if (count > maxCount) {
            maxCount = count;
            mostCommonValue = value;
        }
    }
    return mostCommonValue;
}
