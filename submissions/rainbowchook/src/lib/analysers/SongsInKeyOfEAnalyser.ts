import { Analyser } from "./Analyser";
import type { RowItem } from "../readers/RowItem";

export class SongsInKeyOfECount implements Analyser<RowItem> {
  constructor() {}

  countMatchingRows = (
    header: string,
    value: string,
    data: RowItem[]
  ): number => {
    let sum = data.reduce((acc, currentRow) => {
      if (currentRow[header] === value) {
        acc++
      }
      return acc
    }, 0)
    return sum
  }
  
  run(tracks: RowItem[]) {
    const songsInKeyOfECount = tracks ? this.countMatchingRows('key', 'E', tracks) : 0
    return `The number of songs in the key of E is ${songsInKeyOfECount}.\n`
  }
}