import fs from 'node:fs'
import { DataReader } from './DataReader'

export class CSVFileReader implements DataReader{
  data: string[][] | null = []
  headers: string[] = []

  constructor(public filename: string) {}

  read(headers?: string[]): void {
    try {
      // Load data from CSV file and split into rows by new line into an array of strings
      const csvData = fs
        .readFileSync(this.filename, {
          encoding: 'utf-8',
        })
        .split('\n')

      console.log(
        `Number of lines of pre-cleaned CSV file is ${csvData.length}`
      )
      if (!csvData || csvData.length <= 0) throw new Error('No data found')

      // Clean up data: If there are empty lines, remove them
      // Parse each string row into an array of strings, split by commas that are not enclosed between double quotes
      const csvDataParsed = csvData
        .filter((row: string) => row.length > 0)
        .map((row: string): string[] => {
          const re = /,(?=(?:[^"]*"[^"]*")*[^"]*$)/
          const splitRow = row.split(re)
          return splitRow
        })
        
      // Remove first row of column names/headers if hasHeaders === true
      this.headers = typeof(headers) !== 'undefined' ? headers : csvDataParsed.shift() as string[]
      // console.log('headers: ', this.headers)
      // Each row is mapped from an array of strings into an object, pairing corresponding column names/headers to values as key-value pairs.
      // const csvDataMapped = csvDataParsed.map(this.mapRow)
      // this.data = csvDataMapped
      this.data = csvDataParsed
    } catch (error) {
      console.error(error)
      this.data = null
    }
  }
}
