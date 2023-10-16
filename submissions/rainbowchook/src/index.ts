import { TrackLoader } from './lib/readers/TrackLoader'
import { CountAnalyser } from './lib/analysers/CountAnalyser'
import { ColumnValueCount } from './lib/analysers/ColumnValueCount'
import { CountMaxColumnValueReporter } from './lib/analysers/CountMaxColumnValueReporter'
import { ReportGenerator } from './lib/ReportGenerator.ts/ReportGenerator'
import { Analyser } from './lib/analysers/Analyser'
import { RowItem } from './lib/readers/RowItem'

// Load -> Parse -> Analyse -> Report

// Load + Parse
const reader = TrackLoader.withCSV('spotify-2023.csv')
reader.load()
const tracks = reader.tracks
const trackHeaders = reader.headers

// ReportGenerator = Analyser + Reporter
// Each challenge is addressed by each analyser in sequence:
/*
  Challenges:
  1. Write a script to identify the number of songs in the file.
  2. Write a script that identify the number of songs in the key of E.
  3. Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.
*/
const analysers: Analyser<RowItem>[] = [
  new CountAnalyser(),
  new ColumnValueCount('key', 'E'),
  new CountMaxColumnValueReporter(trackHeaders[1]),
]

for (let analyser of analysers) {
  ReportGenerator.forConsole(analyser).buildAndPrintAnalysisReport(tracks)
  ReportGenerator.forHTML(analyser).buildAndPrintAnalysisReport(tracks)
}
