import parser = require('csv-parse/sync');
import fs = require('fs');

const CSV_FILE_PATH = '../../spotify-2023.csv';

const fileData = fs.readFileSync(CSV_FILE_PATH);

interface Track {
	track_name: string;
	'artist(s)_name': string;
	artist_count: string;
	released_year: string;
	released_month: string;
	released_day: string;
	in_spotify_playlists: string;
	in_spotify_charts: string;
	streams: string;
	in_apple_playlists: string;
	in_apple_charts: string;
	in_deezer_playlists: string;
	in_deezer_charts: string;
	in_shazam_charts: string;
	bpm: string;
	key: string;
	mode: string;
	'danceability_%': string;
	'valence_%': string;
	'energy_%': string;
	'acousticness_%': string;
	'instrumentalness_%': string;
	'liveness_%': string;
	'speechiness_%': string;
}

const records: Track[] = parser.parse(fileData, { columns: true });
console.log(`There are ${records.length} songs in this list.`);

const getCountForValueOfKey = <T, K extends keyof T>(
	list: T[],
	columnName: K,
	columnValue: T[K]
): number => {
	return list.reduce((count, item) => {
		return item[columnName] === columnValue ? count + 1 : count;
	}, 0);
};

const numberOfSongsInhKeyE = getCountForValueOfKey(records, 'key', 'E');
console.log(`There are ${numberOfSongsInhKeyE} songs in the key of E.`);

const highestValueForKey = (
	list: Track[],
	key: keyof Track
): { value: string; count: number } => {
	const listCount = list.reduce<{ [key: string]: number }>((acc, item) => {
		acc[item[key]] ? acc[item[key]]++ : (acc[item[key]] = 1);

		return acc;
	}, {});

	return Object.keys(listCount).reduce<{ value: string; count: number }>(
		(currentHighest, key) => {
			return currentHighest.count && currentHighest.count > listCount[key]
				? currentHighest
				: { value: key, count: listCount[key] };
		},
		{} as { value: string; count: number }
	);
};

const mostPopularArtist = highestValueForKey(records, 'artist(s)_name');
console.log(
	`The most popular artist is ${mostPopularArtist.value} with ${mostPopularArtist.count} songs.`
);
