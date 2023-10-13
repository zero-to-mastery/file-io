import { DataReader } from './DataReader'
import { CSVFileReader } from './CSVFileReader'
import type { RowItem } from '../RowItem'

export class TrackReader {
  tracks: RowItem[] = []
  headers: string[] = []
  constructor(public reader: DataReader) {}

  static withCSV(filename: string) {
    return new TrackReader(new CSVFileReader('spotify-2023.csv'))
  }

  // loads headers if any; otherwise headers are extracted from first line of CSV file
  load(headers?: string[]) {
    headers ? this.reader.read(headers) : this.reader.read()
    // parse data into array of RowItem objects for analysis later
    this.tracks = this.reader.data
      ? this.reader.data.map((row: string[]): RowItem => {
          // console.log(this.reader.headers)
          let returnObject: RowItem = {}
          for (let j = 0; j < this.reader.headers.length; j++) {
            returnObject[this.reader.headers[j]] = row[j]
          }
          return returnObject
        })
      : []
  }
}
