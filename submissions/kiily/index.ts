import fs from 'fs';
import csv from 'csv-parser';

type Song = {
	key: string;
	released_day: string;
	track_name: string;
};

type SongField = keyof Song;

const songs: Song[] = [];
const filterByEKey = (song: Song) => {
	return song.key === 'E';
};

const runSpotifyDataLogger = () => {
	fs.createReadStream('./spotify-2023.csv')
		.pipe(csv())
		.on('data', (row: Song) => {
			songs.push(row);
		})
		.on('end', () => {
			console.info(`[CHALLENGE 1]: Total number of songs: [${songs.length}]`);
			console.info(
				`[CHALLENGE 2]: Total number of songs starting with the E key: [${
					songs.filter(filterByEKey).length
				}]`
			);

			const fieldToCount = 'released_day';
			const songsMap: Record<string, number> = {};
			let maxValue = 0;
			let maxOccurencesItem: Song | null = null;
			for (const song of songs) {
				const key = song[fieldToCount] as SongField;
				if (!songsMap[key]) {
					songsMap[key] = 1;
				} else {
					songsMap[key] += 1;
				}
				if (songsMap[key] > maxValue) {
					maxValue = songsMap[key];
					maxOccurencesItem = song;
				}
			}
			if (maxOccurencesItem) {
				console.info(
					`[CHALLENGE 3]: The most common value for "${fieldToCount}" is "${maxOccurencesItem.track_name}" with ${maxValue} occurences`
				);
			}
		});
};

runSpotifyDataLogger();
