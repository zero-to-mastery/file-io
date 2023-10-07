const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

const results = [];
const trackInfo = {
  numberOfSongs: 0,
  numberOfKeyESongs: 0,
  mostCommonName: '',
};

const countSongKey = (data, keyValue) => {
  const result = data.reduce((acc, { key }) => {
    if (key === keyValue) {
      acc += 1;
    }

    return acc;
  }, 0);

  return result;
};

const getMostCommonName = (data) => {
  const nameCount = data.reduce((acc, track) => {
    const artistName = track['artist(s)_name'];

    acc[artistName] ? (acc[artistName] += 1) : (acc[artistName] = 1);

    return acc;
  }, {});

  const nameCountArray = Object.entries(nameCount);

  let mostCommonNameCount = 0;
  let mostCommonName = '';

  nameCountArray.forEach((name) => {
    if (name[1] > mostCommonNameCount) {
      mostCommonNameCount = name[1];
      mostCommonName = name[0];
    }
  });

  return mostCommonName;
};

fs.createReadStream(path.resolve(__dirname, '../../spotify-2023.csv'))
  .pipe(csv())
  .on('data', (data) => results.push(data))
  .on('end', () => {
    trackInfo.numberOfSongs = results.length;
    trackInfo.numberOfKeyESongs = countSongKey(results, 'E');
    trackInfo.mostCommonName = getMostCommonName(results);

    console.log(trackInfo);
  });

