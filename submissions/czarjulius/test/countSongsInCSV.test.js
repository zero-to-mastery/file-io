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

  it('should count the number of songs in the key of E', async () => {
    const result = await spotifyDataAnalyzer(csvFilePath, { key: 'E' });
    expect(result.keyESongs).toBe(2);
  });

  it('should count the occurrences of artist(s) and determine the most common value', async () => {
    const result = await spotifyDataAnalyzer(csvFilePath, { columnToCount: 'artist(s)_name' });
    expect(result.mostCommonValue).toBe('julius');
    expect(result.highestCount).toBe(2);
  });
});
