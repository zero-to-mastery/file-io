import { Analyser } from "./Analyser";
import type { RowItem } from "../readers/RowItem";

export class ColumnValueCount implements Analyser<RowItem> {
  constructor(public column: string, public value: string) {}

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
    const count = tracks ? this.countMatchingRows(this.column, this.value, tracks) : 0
    return `The number of songs in column "${this.column}" with value "${this.value}" is ${count}.\n`
  }
}