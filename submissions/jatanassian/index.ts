import parser = require('csv-parse/sync');
import fs = require('fs');

const CSV_FILE_PATH = '../../spotify-2023.csv';

// ===================================================
// Interfaces
// ===================================================

interface SpotifyTrack {
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

interface HighestValueForKeyOutput {
	value: string;
	count: number;
}

// ===================================================
// Functions
// ===================================================

/**
 * Read and parse CSV file
 *
 * @template T object
 * @param {string} filePath path to the CSV file
 * @returns {T[]} list of the specified type
 */
const readCsvFile = <T>(filePath: string): T[] => {
	const fileData = fs.readFileSync(filePath);
	return parser.parse(fileData, { columns: true });
};

/**
 * Counts how many time an array of object has a specific value for the given object's key
 *
 * @template T - object
 * @template K - key of the T object
 * @param {T[]} list - array of objects of T type
 * @param {K} key - a property of the T object
 * @param {T[K]} value
 * @returns {number}
 */
const getCountForValueOfKey = <T, K extends keyof T>(
	list: T[],
	key: K,
	value: T[K]
): number => {
	return list.reduce((count, item) => {
		return item[key] === value ? count + 1 : count;
	}, 0);
};

/**
 * For a given property/key, return the most common value and its count
 *
 * @template T - object
 * @param {T[]} list - array of objects
 * @param {keyof T} key - one of the object's property
 * @returns
 */
const highestValueForKey = <T>(
	list: T[],
	key: keyof T
): HighestValueForKeyOutput => {
	// Count how many times each value appears
	const listCount = list.reduce<{ [field: string]: number }>((acc, item) => {
		const value = String(item[key]);
		acc[value] ? acc[value]++ : (acc[value] = 1);

		return acc;
	}, {});

	// Return the value with the highest count
	return Object.keys(listCount).reduce<HighestValueForKeyOutput>(
		(currentHighest, key) => {
			return currentHighest.count && currentHighest.count > listCount[key]
				? currentHighest
				: { value: key, count: listCount[key] };
		},
		{} as HighestValueForKeyOutput
	);
};

// ===================================================
// Flow
// ===================================================

// Challenge #1
const records = readCsvFile<SpotifyTrack>(CSV_FILE_PATH);
console.log(`There are ${records.length} songs in this list.`);

// Challenge #2
const numberOfSongsInKeyE = getCountForValueOfKey<SpotifyTrack, 'key'>(
	records,
	'key',
	'E'
);
console.log(`There are ${numberOfSongsInKeyE} songs in the key of E.`);

// Challenge #3
const mostPopularArtist = highestValueForKey<SpotifyTrack>(
	records,
	'artist(s)_name'
);
console.log(
	`The most popular artist is ${mostPopularArtist.value} with ${mostPopularArtist.count} songs.`
);
