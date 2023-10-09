const csv = require('csv-parser')
const fs = require('fs')
const results = []

function getNumberOfSongs(results, key) {
    let resultsToCount = [...results]
  
    if(key){
      resultsToCount = resultsToCount.filter((record) => record.key === key) 
    }
    return resultsToCount.length;
}

function getMostOccurrences(valueToAnalize, results) {
  let mostCommonValue = ''
  let maxValue = 0
  let counter = {}
  for(const record of results){
      const countValue = record[valueToAnalize];
      counter[countValue] = (counter[countValue] || 0 ) + 1

      if(counter[countValue] > maxValue){
          maxValue = counter[countValue] 
          mostCommonValue = countValue
      }
  }
  return  { mostCommonValue ,maxValue };
}

fs.createReadStream('./spotify-2023.csv').pipe(csv())
.on('data', (data) => results.push(data))
.on('end', () => {
  const {mostCommonValue ,maxValue  } = getMostOccurrences('artist(s)_name', results)
  console.log('Total songs: '  + getNumberOfSongs(results));
  console.log('Total songs with E key: ' + getNumberOfSongs(results, 'E'));
  console.log('Most commom value: ' + mostCommonValue + ' with ' + maxValue + ' incidences');

});
