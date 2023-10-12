import fs from 'node:fs'

type RowItem = {
  [key: string]: string
}

export class CSVFileReader {
  data: RowItem[] | null = []
  headers: string[] = []
  
  constructor(public filename: string) {}

  read(): void {
    try {
      // Load data from CSV file and split into rows by new line into an array of strings
      const csvData = fs
        .readFileSync(this.filename, {
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
      this.headers = headers
  
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
  
      this.data = csvDataMapped
    } catch (error) {
      this.data = null
    }
  }
}