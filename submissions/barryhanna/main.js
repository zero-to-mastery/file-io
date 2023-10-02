import { readFileSync } from 'fs';
import { parse } from 'csv-parse/sync';

const KEY = 'E';
const COUNT_COLUMN = 'artist(s)_name';

const spotifyData = parse(readFileSync('./spotify-2023.csv'), {
	columns: true,
	skip_empty_lines: true,
});

const getNumberOfSongs = (songData) => songData.length;

const getNumberOfSongsInKey = (songData, key) =>
	songData.filter((song) => song.key === key).length;

const getMostPopularArtist = (songData) => {
	const sortedArtistsWithSongTotal = Object.entries(
		songData.reduce((acc, val) => {
			const artistName = val[COUNT_COLUMN];
			if (!acc[artistName]) {
				acc[artistName] = 1;
			} else {
				acc[artistName] += 1;
			}
			return acc;
		}, {})
	).sort((a, b) => b[1] - a[1]);
	return {
		artist: sortedArtistsWithSongTotal[0][0],
		songs: sortedArtistsWithSongTotal[0][1],
	};
};

console.log(
	`Total number of songs: ${getNumberOfSongs(spotifyData)}`
);
console.log(
	`Number of songs in key of ${KEY}: ${getNumberOfSongsInKey(
		spotifyData,
		KEY
	)}`
);

const artistWithMostSongs = getMostPopularArtist(spotifyData);
console.log(
	`The most popular artist is ${artistWithMostSongs.artist} with ${artistWithMostSongs.songs} songs.`
);
