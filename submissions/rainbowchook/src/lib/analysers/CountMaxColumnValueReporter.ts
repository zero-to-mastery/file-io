import { Analyser } from './Analyser'
import type { RowItem } from '../readers/RowItem'
import type { ValuesArrayType } from './ValuesArrayType'

export class CountMaxColumnValueReporter implements Analyser<RowItem> {
  constructor(public column: string) {}

  maxColumnValue = (
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

  reportColValueCount = (col: string, tracks: RowItem[]): string => {
    const { column, uniqueColValuesArray, maxColValueArray } = tracks
      ? this.maxColumnValue(col, tracks)
      : { column: col, uniqueColValuesArray: [], maxColValueArray: [] }

    let returnString = ''

    if (uniqueColValuesArray.length <= 0) {
      return returnString.concat(
        `The column name, "${column}", does not exist.  Try again.`
      )
    }

    returnString = returnString.concat(`Unique values of column name, "${column}":\n`)

    for (let row of uniqueColValuesArray) {
      returnString = returnString.concat(`Value, ${row.value}, occurs ${row.count} times.\n`)
    }

    for (let row of maxColValueArray) {
      returnString = returnString.concat(
        `The most common value, ${row.value}, occurs ${row.count} times.\n`
      )
    }
  
    return returnString
  }

  run(tracks: RowItem[]): string {
    return this.reportColValueCount(this.column, tracks)
  }
}
