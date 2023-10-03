import fs from "node:fs/promises";
import path from "node:path";
import { parse } from "csv-parse";

const csvFilePath = path.join(__dirname, "..", "data", "spotify-2023.csv");

let songsKeyE = 0;
let maxArtistName = "";
let maxArtistCount = 0;

const artistNameCount: any = {};
const artistSet = new Set();

const headers = [
  "track_name",
  "artist_name",
  "artist_count",
  "released_year",
  "released_month",
  "released_day",
  "in_spotify_playlists",
  "in_spotify_charts",
  "streams",
  "in_apple_playlists",
  "in_apple_charts",
  "in_deezer_playlists",
  "in_deezer_charts",
  "in_shazam_charts",
  "bpm",
  "key",
  "mode",
  "danceability",
  "valence",
  "energy",
  "acousticness",
  "instrumentalness",
  "liveness",
  "speechiness",
];

type SongType = {
  track_name: string;
  artist_name: string;
  artist_count: number;
  released_year: number;
  released_month: number;
  released_day: number;
  in_spotify_playlists: number;
  in_spotify_charts: number;
  streams: number;
  in_apple_playlists: number;
  in_apple_charts: number;
  in_deezer_playlists: number;
  in_deezer_charts: number;
  in_shazam_charts: number;
  bpm: number;
  key: string;
  mode: string;
  danceability: number;
  valence: number;
  energy: number;
  acousticness: number;
  instrumentalness: number;
  liveness: number;
  speechiness: number;
};

async function loadData() {
  let fileContent;
  try {
    fileContent = await fs.readFile(csvFilePath, { encoding: "utf-8" });

    parse(
      fileContent,
      {
        delimiter: ",",
        columns: headers,
        from: 2,
      },
      (error: Error, songs: SongType[]) => {
        if (error) {
          console.error(error);
        }
        for (let song of songs) {
          artistSet.add(song.artist_name);
          if (artistNameCount[song.artist_name]) {
            artistNameCount[song.artist_name] =
              artistNameCount[song.artist_name] + 1;
          } else {
            artistNameCount[song.artist_name] = 1;
          }

          if (song.key === "E") {
            songsKeyE++;
          }
        }

        for (let artist of artistSet) {
          if (artistNameCount[String(artist)] > maxArtistCount) {
            maxArtistCount = artistNameCount[String(artist)];
            maxArtistName = String(artist);
          }
        }

        console.log(`There are ${songs.length} songs in the file`);
        console.log(`There are ${songsKeyE} songs in the file with key of E`);
        console.log(
          `The artist ${maxArtistName} is the famous with ${maxArtistCount} songs`
        );
      }
    );
  } catch (err) {
    console.error(err);
    throw err;
  }
}

loadData();
