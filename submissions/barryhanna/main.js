const fs = require('fs');
const { parse } = require('csv-parse/sync');

const KEY = 'E';
const COUNT_COLUMN = 'artist(s)_name';

const spotifyData = parse(fs.readFileSync('./spotify-2023.csv'), {
	columns: true,
	skip_empty_lines: true,
});

console.log(`Total number of songs: ${spotifyData.length}`);
const songsInKey = spotifyData.filter(
	(song) => song.key === KEY
).length;
console.log(`Number of songs in key of ${KEY}: ${songsInKey}`);

const totals = spotifyData.reduce((acc, val) => {
	const artistName = val[COUNT_COLUMN];
	if (!acc[artistName]) {
		acc[artistName] = 1;
	} else {
		acc[artistName] += 1;
	}
	return acc;
}, {});

const sorted = Object.entries(totals).sort((a, b) => b[1] - a[1]);

console.log(
	`The most popular artist is ${sorted[0][0]} with ${sorted[0][1]} songs.`
);
