import fs from 'node:fs'

type RowItem = {
  [key: string]: string
}

type ValuesArrayType = {
  value: string
  count: number
}

const loadData = (): RowItem[] | null => {
  try {
    // Load data from CSV file and split into rows by new line into an array of strings
    const csvData = fs
      .readFileSync('spotify-2023.csv', {
        encoding: 'utf-8',
      })
      .split('\n')

    console.log(`Number of lines of pre-cleaned CSV file is ${csvData.length}`)
    if (!csvData || csvData.length <= 0) throw new Error('No data found')

    // Clean up data: If there are empty lines, remove them
    const csvDataWithoutEmptyLines = csvData.filter(
      (row: string) => row.length > 0
    )

    // Parse each string row into an array of strings, split by commas that are not enclosed between double quotes
    const csvDataParsed = csvDataWithoutEmptyLines.map(
      (row: string): string[] => {
        const re = /,(?=(?:[^"]*"[^"]*")*[^"]*$)/
        const splitRow = row.split(re)
        return splitRow
      }
    )

    // Remove first row of column names/headers
    const headers: string[] = csvDataParsed.shift()!

    // Each row is mapped from an array of strings into an object, pairing corresponding column names/headers to values as key-value pairs.
    const csvDataMapped = csvDataParsed.map((row: string[], i: number) => {
      let returnObject: RowItem = {}
      // if(i === (csvDataParsed.length - 1)) {
      //   console.log(row)
      // }
      for (let j = 0; j < headers.length; j++) {
        // if(row[j] === '') {
        //   console.log([i, row[0], j, headers[j], row[j]])
        // }
        returnObject[headers[j]] = row[j]
      }
      return returnObject
    })

    // console.log('tracks: ')
    // console.log(headers)
    // console.log(csvDataMapped[24].length)
    // console.log(csvDataMapped[24])

    return csvDataMapped
  } catch (error) {
    return null
  }
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
  if (!data.length) {
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

//Reporting
const tracks = loadData()
const trackCount = tracks ? countRows(tracks) : 0
const songsInKeyOfECount = tracks ? countMatchingRows('key', 'E', tracks) : 0

console.log(`The number of songs in the file is ${trackCount}.`)
console.log(`The number of songs in the key of E is ${songsInKeyOfECount}.`)

const reportColValueCount = (col: string): void => {
  const { column, uniqueColValuesArray, maxColValueArray } = tracks
    ? maxColumnValue(col, tracks)
    : { column: col, uniqueColValuesArray: [], maxColValueArray: [] }
  console.log(`Unique values of column name, ${column} ${uniqueColValuesArray.length}:`)
  console.log(uniqueColValuesArray)
  if (uniqueColValuesArray.length <= 0) {
    console.log(`The column name ${column} does not exist`)
  } else {
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

reportColValueCount('1%')
