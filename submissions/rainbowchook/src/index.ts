import { TrackReader } from './lib/readers/TrackReader'
import { RowItem } from './lib/RowItem'

// Load -> Parse -> Analyse -> Report

type ValuesArrayType = {
  value: string
  count: number
}

const countRows = (rows: RowItem[]): number => {
  return rows.length
}

const countMatchingRows = (
  header: string,
  value: string,
  data: RowItem[]
): number => {
  //or use Array.reduce()
  // let count = 0
  // data.forEach((row: RowItem): void => {
  //   if(row[header] === value) {
  //     count++
  //   }
  // })
  // return count

  let sum = data.reduce((acc, currentRow) => {
    if (currentRow[header] === value) {
      acc++
    }
    return acc
  }, 0)
  return sum
}

const maxColumnValue = (
  column: string,
  data: RowItem[]
): {
  column: string
  maxColValueArray: ValuesArrayType[]
  uniqueColValuesArray: ValuesArrayType[]
} => {
  const uniqueColValuesArray: ValuesArrayType[] = []
  if (!data.length || !data[0][column]) {
    return {
      column,
      maxColValueArray: [],
      uniqueColValuesArray,
    }
  }
  /* 
    A) Iterate through each row of the data passed in: (Alternative use a Map for unique key-value pairs)
    1. Compare new value with existing values in the valuesArray (Use Array.find())
    2. a) For each new value, push the value and count into the valuesArray as a hash map
    2. b) For a new value that already exists in the valuesArray, increment the count
    
    B) Iterate through each row of the valuesArray: 
    1. Use Array.sort() to sort items from smallest-largest count (compareFn compares count).
    2. Check the count of the last item in the Array (item with the largest count)
    3. Check if there are any other items with the same count.  
    4. Return an array with the item(s) with the largest count.
  */

  //Get a Map of unique column values and their count - increment count for found values
  const colValuesMap = new Map<string, number>()
  for (let row of data) {
    const colValue = row[column]
    if (!colValuesMap.has(colValue)) {
      colValuesMap.set(colValue, 1)
    } else {
      let currentCount = colValuesMap.get(colValue)
      if (currentCount) {
        currentCount++
        colValuesMap.set(colValue, currentCount)
      }
    }
  }

  //Convert Map into uniqueColValuesArray
  for (const [value, count] of colValuesMap) {
    uniqueColValuesArray.push({ value, count })
  }

  //Sort uniqueColValuesArray from smallest to largest count
  uniqueColValuesArray.sort(
    (a: ValuesArrayType, b: ValuesArrayType): number => {
      return a.count === b.count ? 0 : a.count > b.count ? 1 : -1
    }
  )
  //Get largest count
  const maxCount = uniqueColValuesArray[uniqueColValuesArray.length - 1].count

  //Filter uniqueColValuesArray to return elements that contain the largest count (count of last element)
  const maxColValueArray: ValuesArrayType[] = uniqueColValuesArray.filter(
    (value: ValuesArrayType) => value.count === maxCount
  )
  return { column, uniqueColValuesArray, maxColValueArray }
}

/*
  Challenges:
  1. Write a script to identify the number of songs in the file.
  2. Write a script that identify the number of songs in the key of E.
  3. Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.
*/

//Reporting = Analyser + Reporter
// const reader = new TrackReader(new CSVFileReader('spotify-2023.csv'))
const reader = TrackReader.withCSV('spotify-2023.csv')
reader.load()
const tracks = reader.tracks
const trackHeaders = reader.headers
const trackCount = tracks ? countRows(tracks) : 0
const songsInKeyOfECount = tracks ? countMatchingRows('key', 'E', tracks) : 0

console.log(`The number of songs in the file is ${trackCount}.`)
console.log(`The number of songs in the key of E is ${songsInKeyOfECount}.`)

const reportColValueCount = (col: string): void => {
  const { column, uniqueColValuesArray, maxColValueArray } = tracks
    ? maxColumnValue(col, tracks)
    : { column: col, uniqueColValuesArray: [], maxColValueArray: [] }
  if (uniqueColValuesArray.length <= 0) {
    console.log(`The column name, ${column}, does not exist.  Try again.`)
  } else {
    console.log(`Unique values of column name, ${column}:`)
    for (let row of uniqueColValuesArray) {
      console.log(`Value, ${row.value}, occurs ${row.count} times.`)
    }
    for (let row of maxColValueArray) {
      console.log(
        `The most common value, ${row.value}, occurs ${row.count} times.`
      )
    }
  }
}

reportColValueCount(trackHeaders[10])
