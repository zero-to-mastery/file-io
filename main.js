const fs = require('fs');
const { parse } = require('csv-parse/sync');
const {
	getNumberOfSongs,
	getNumberOfSongsInKey,
	getMostPopularArtist,
} = require('./song-stats.js');

const KEY = 'E';
const COUNT_COLUMN = 'artist(s)_name';

const spotifyData = parse(fs.readFileSync('./spotify-2023.csv'), {
	columns: true,
	skip_empty_lines: true,
});

const artistWithMostSongs = getMostPopularArtist(
	spotifyData,
	COUNT_COLUMN
);

function main() {
	console.log(
		`Total number of songs: ${getNumberOfSongs(spotifyData)}`
	);
	console.log(
		`Number of songs in key of ${KEY}: ${getNumberOfSongsInKey(
			spotifyData,
			KEY
		)}`
	);
	console.log(
		`The most popular artist is ${artistWithMostSongs.artist} with ${artistWithMostSongs.songs} songs.`
	);
}

main();
