import { DataReader } from './DataReader'
import { CSVFileReader } from './CSVFileReader'
import type { RowItem } from './RowItem'

export class TrackLoader {
  tracks: RowItem[] = []
  headers: string[] = []
  constructor(public reader: DataReader) {}

  static withCSV(filename: string) {
    return new TrackLoader(new CSVFileReader(filename))
  }

  // loads headers if any; otherwise headers are extracted from first line of CSV file
  load(headers?: string[]) {
    headers ? this.reader.read(headers) : this.reader.read()
    // parse data into array of RowItem objects for analysis later
    // Each row is mapped from an array of strings into a RowItem object, pairing corresponding column names/headers to values as key-value pairs.
    this.tracks = this.reader.data
      ? this.reader.data.map((row: string[]): RowItem => {
          let returnObject: RowItem = {}
          for (let j = 0; j < this.reader.headers.length; j++) {
            returnObject[this.reader.headers[j]] = row[j]
          }
          return returnObject
        })
      : []
    this.headers = headers ? headers : this.reader.headers
  }
}
