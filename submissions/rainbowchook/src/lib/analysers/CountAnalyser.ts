import { Analyser } from './Analyser'
import type { RowItem } from '../readers/RowItem'

export class CountAnalyser implements Analyser<RowItem> {
  constructor() {}

  countRows = (rows: RowItem[]): number => {
    return rows.length
  }

  run(tracks: RowItem[]): string {
    const trackCount = tracks ? this.countRows(tracks) : 0
    return `The number of songs in the file is ${trackCount}.\n`
  }

}
