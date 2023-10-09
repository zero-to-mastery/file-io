// run this program via node (node run.js)
// the parameters for the first 2 challenges are hard coded, so those will run as is
// to include the third challenge you need to pass an additional argument (node run.js "example")
// the additional argument must be a string that matches one of the properties of the track object, otherwise it will return undefined

const csv = require('csv-parser')
const fs = require('fs')
const process = require('process')
const results = []
// setting a variable that is passed via the command line
let val
if (process.argv[2]) {
  val = process.argv[2].toString()
}

// counting number of songs with a specified key
const getAmountOfSongsWithKey = (list, key) => {
  let amountInKey = 0
  list.forEach(element => {
    if (element.key == key) amountInKey++
  })
  return amountInKey
}
// return highest occuring values in a column
// takes object with unique values as properties and their respective duplicate score as the value, returns an array of properties with the highest score
const getMostCommonValue = obj => {
  let highestScore = 0
  let keysWithHighestScore = []
  for (const key in obj) {
    //console.log(obj[key])
    if (obj[key] > highestScore) {
      highestScore = obj[key]
    }
  }
  for (const key in obj) {
    if (obj[key] == highestScore) {
      keysWithHighestScore.push(key)
    }
  }
  console.log('The highest occuring duplicate score is: ', highestScore)
  return keysWithHighestScore
}

// counting and returning most common value in a specified column
const getMostCommonValueInColumn = (list, prop) => {
  let valuesInColumnScore = {}
  list.forEach(element => {
    if (element[prop] in valuesInColumnScore) {
      valuesInColumnScore[element[prop]]++
    } else {
      valuesInColumnScore[element[prop]] = 1
    }
  })
  //console.log(valuesInColumnScore)
  return getMostCommonValue(valuesInColumnScore)
}

// reading from file (spotify-2023.csv) and evaluating it's content according to given requirements
//
fs.createReadStream('spotify-2023.csv')
  .pipe(csv())
  .on('data', data => results.push(data))
  .on('end', () => {
    console.log(results[0]) // the parser returns an array cotaining objects, each of them representing a track
    console.log('Number of songs in this file: ', results.length) // determining the count of tracks, therefore you shall determine the lenght of the array
    // the following iterates through the entire array and counts each track with E as their Key
    console.log(
      'Amount of songs in the Key of "E" is: ',
      getAmountOfSongsWithKey(results, 'E')
    )
    // the following evaluates a given key and makes an object containing the values and their respective duplicate score, afterwards and array is returned containing the highest occuring values
    console.log('Value is set to: ', val)
    if (val) {
      console.log(
        'Most common',
        val,
        'in the column are: ',
        getMostCommonValueInColumn(results, val)
      )
    } else {
      console.log('There is no value set, skipping that part.')
    }
  })
