const spotifyDataAnalyzer = require('../spotifyDataAnalyzer');
const path = require('path');

describe('spotifyDataAnalyzer', () => {
  const csvFilePath = path.join(__dirname, 'dummyData.csv');
  it('should count the number of songs in the CSV file', async () => {
    const result = await spotifyDataAnalyzer(csvFilePath);
    expect(result.totalSongs).toBe(3);
  });

  it('should handle errors gracefully', async () => {
    const WrongCSVFilePath = 'nonexistentfile.csv';
    try {
      await spotifyDataAnalyzer(WrongCSVFilePath);
    } catch (error) {
      expect(error).toBeDefined();
    }
  });
});
