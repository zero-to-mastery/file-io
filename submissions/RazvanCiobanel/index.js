import * as fs from "fs";
import CsvParser from "csv-parser";

const csv = CsvParser;
const file = "../../spotify-2023.csv";
let results = []

function getData(file, type) {
  let results = [];
  return new Promise((resolve, reject) => {
    fs.createReadStream(file)
      .on("error", (error) => {
        reject(error);
      })
      .pipe(csv())
      .on("data", (data) => results.push(data))
      .on("end", () => {
        resolve(results);
      });
  });
}

const getSongs = async () => {
  const songs = await getData(file);
  results = songs 
  // 1 Identify the number of songs in the file
  const totalSongs = results.length
  console.log("Number of songs: ", totalSongs)
  // Number of songs in the key of E
  const newArr = [...results]
  const keyE = newArr.filter(item => item.key === 'E')
  const songsInE = keyE.length
  console.log("Number of songs in the key of E: ", songsInE)
};

getSongs();

