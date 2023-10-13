import { TrackReader } from './lib/readers/TrackReader'
import { CountAnalyser } from './lib/analysers/CountAnalyser'
import { ColumnValueCount } from './lib/analysers/ColumnValueCount'
import { CountMaxColumnValueReporter } from './lib/analysers/CountMaxColumnValueReporter'
import { ReportGenerator } from './lib/ReportGenerator.ts/ReportGenerator'

// Load -> Parse -> Analyse -> Report

/*
  Challenges:
  1. Write a script to identify the number of songs in the file.
  2. Write a script that identify the number of songs in the key of E.
  3. Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.
*/

//ReportGenerator = Analyser + Reporter
// const reader = new TrackReader(new CSVFileReader('spotify-2023.csv'))
const reader = TrackReader.withCSV('spotify-2023.csv')
reader.load()
const tracks = reader.tracks
const trackHeaders = reader.headers
// const trackCount = tracks ? countRows(tracks) : 0
// const songsInKeyOfECount = tracks ? countMatchingRows('key', 'E', tracks) : 0

// console.log(`The number of songs in the file is ${trackCount}.`)
// console.log(`The number of songs in the key of E is ${songsInKeyOfECount}.`)

// reportColValueCount(trackHeaders[1])

// console.log(new CountAnalyser().run(tracks))
// console.log(new SongsInKeyOfECount().run(tracks))
// console.log(trackHeaders)
// console.log(new CountMaxColumnValueReporter(trackHeaders[17]).run(tracks))

// const consoleReporter = new ConsoleReport()
// consoleReporter.print(new CountAnalyser().run(tracks))
// consoleReporter.print(new SongsInKeyOfECount().run(tracks))
// consoleReporter.print(new CountMaxColumnValueReporter(trackHeaders[17]).run(tracks))

// consoleReporter.print(new CountAnalyser().run(tracks) + new SongsInKeyOfECount().run(tracks) + new CountMaxColumnValueReporter(trackHeaders[17]).run(tracks))

// new ReportGenerator(new CountAnalyser(), new ConsoleReport()).buildAndPrintAnalysisReport(tracks)
// new ReportGenerator(new SongsInKeyOfECount(), new ConsoleReport()).buildAndPrintAnalysisReport(tracks)
// new ReportGenerator(new CountMaxColumnValueReporter(trackHeaders[1]), new ConsoleReport()).buildAndPrintAnalysisReport(tracks)

ReportGenerator.forConsole(new CountAnalyser()).buildAndPrintAnalysisReport(tracks)
ReportGenerator.forConsole(new ColumnValueCount('key', 'G')).buildAndPrintAnalysisReport(tracks)
ReportGenerator.forConsole(new CountMaxColumnValueReporter(trackHeaders[16])).buildAndPrintAnalysisReport(tracks)