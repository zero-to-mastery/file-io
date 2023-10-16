import fs from 'node:fs'
import { Reporter } from './Reporter'
import { getDate } from '../utils'

export class HTMLReporter implements Reporter {
  print(report: string): void {
    const newReport = report
      .split('\n')
      .filter((row: string): boolean => row.length > 0)
      .join('<br />')
    console.log(newReport)
    const html = `
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
      </head>
      <body>
      <h1>Analysis Report</h1>
      <div>
        ${newReport}
      </div>
      </body>
      </html>
    `
    
    fs.writeFileSync(
      `report-${getDate()}${new Date().getUTCMilliseconds()}.html`,
      html
    )
  }
}
