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
console.log(`This file contains ${records.length} songs.`);

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
