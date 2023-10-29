import csvParser from 'csv-parser';
import * as fs from 'fs';
import { Song } from './types';

const readCsv: () => Promise<Song[]> = () => {
  return new Promise((resolve, reject) => {
    const data: Song[] = [];
    fs.createReadStream('spotify-2023.csv')
      .pipe(csvParser())
      .on('data', (song) => data.push(song))
      .on('end', () => {
        resolve(data);
      })
      .on('error', () => {
        reject('Failed to read CSV');
      });
  });
};

const main = async () => {
  try {
    const songs = await readCsv();

    // Challenges
    // 1. Write a script to identify the number of songs in the file.

    // Just find the length of the array (953)
    console.log(`The number of songs: ${songs.length}`);

    // 2. Write a script that identify the number of songs in the key of E.

    // Use the reduce method to find the number of songs in the key of E (62)
    const numOfSongInTheKeyOfE = songs.reduce(
      (curr, { key }) => (key === 'E' ? curr + 1 : curr),
      0
    );
    console.log(`The number of songs in the key of E: ${numOfSongInTheKeyOfE}`);

    // 3. Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.

    // Use the reduce method to create an object literal, where the key is the key of the song and the value is also a hashmap of the value and the number of the occurences

    const results = songs.reduce((curr, song) => {
      Object.entries(song).forEach(([key, value]) => {
        curr[key] = curr[key] ?? {};
        curr[key][value] = (curr[key][value] ?? 0) + 1;
      });

      return curr;
    }, {} as Record<string, Record<string, number>>);

    Object.entries(results).forEach(([key, occurenceMap]) => {
      const mostCommonValue = Object.entries(occurenceMap).sort(
        (a, b) => b[1] - a[1]
      )[0];
      console.log(
        `The most common value for ${key}: ${mostCommonValue[0]}. Occurences: ${mostCommonValue[1]}`
      );
    });
  } catch (error: any) {
    console.log(error);
  }
};

main();
