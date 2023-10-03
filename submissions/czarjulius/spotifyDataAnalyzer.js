const fs = require('fs');
const parse = require('csv-parser');

const spotifyDataAnalyzer = async (csvFilePath) => {
  if (!fs.existsSync(csvFilePath)) {
    throw new Error(`CSV file not found: ${csvFilePath}`);
  }

  let songCount = 0;

  const stream = fs
    .createReadStream(csvFilePath)
    .pipe(
      parse({
        columns: true,
      })
    )
    .on('data', () => {
      songCount++;
    });

  return new Promise((resolve, reject) => {
    stream
      .on('end', () => {
        const result = {
          totalSongs: songCount,
        };
        resolve(result);
      })
      .on('error', (error) => reject('Something went wrong!', error));
  });
};

module.exports = spotifyDataAnalyzer;
