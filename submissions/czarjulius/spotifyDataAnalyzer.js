const fs = require('fs');
const parse = require('csv-parser');

async function spotifyDataAnalyzer(csvFilePath, options = {}) {
  if (!fs.existsSync(csvFilePath)) {
    throw new Error(`CSV file not found: ${csvFilePath}`);
  }

  let songCount = 0;
  let keyESongCount = 0;
  const valueCounts = {};

  const { key, columnToCount } = options;

  const stream = fs
    .createReadStream(csvFilePath)
    .pipe(
      parse({
        columns: true,
      })
    )
    .on('data', (row) => {
      songCount++;

      if (key && row['key'] && row['key'].toUpperCase() === key.toUpperCase()) {
        keyESongCount++;
      }

      const columnValue = row[columnToCount];
      if (columnValue) {
        const normalizedValue = columnValue.toLowerCase();
        valueCounts[normalizedValue] = (valueCounts[normalizedValue] || 0) + 1;
      }
    });

  return new Promise((resolve, reject) => {
    stream
      .on('end', () => {
        let mostCommonValue = '';
        let highestCount = 0;
        for (const value in valueCounts) {
          if (valueCounts[value] > highestCount) {
            mostCommonValue = value;
            highestCount = valueCounts[value];
          }
        }
        const result = {
          totalSongs: songCount,
          keyESongs: keyESongCount,
          mostCommonValue,
          highestCount,
        };
        resolve(result);
      })
      .on('error', (error) => reject('Something went wrong!', error));
  });
}

module.exports = spotifyDataAnalyzer;
