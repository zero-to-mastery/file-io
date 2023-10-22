# Spotify Analysis in TypeScript

## Description

This application parses a Spotify CSV file and produces analysis reports through console logging and generating HTML reports according to the challenge tasks.

The process from reading the CSV file to the report generation follows thus: 

Load -> Parse -> Analyse -> Report

Written with code reuse in mind, this application utilises interfaces to delegate specific tasks.

### Load + Parse

1. A TrackLoader loads the data read by CSVFileReader (implements DataReader interface) by parsing it into an array of RowItem objects. If an array of headers/column_names is not passed into the `load()` method, the first line of the CSV file will be assumed to be the list of headers/column_names.

2. The tracks and trackHeaders are extracted from the TrackReader object fields for use by the ReportGenerator in the main file `index.ts`.

```typescript
const reader = TrackLoader.withCSV('spotify-2023.csv')
reader.load()
const tracks = reader.tracks
const trackHeaders = reader.headers
```

### Analyse + Report

1. A ReportGenerator coordinates the results analysis and reporting modes. ReportGenerator has static methods `forConsole()` and `forHTML()` that can be invoked for a specific analyser, returning instances of ReportGenerator with different reporting modes.

2. For each challenge task, individual analysers implementing the Analyser interface were created.

3. Different reporting modes can also be passed into the ReportGenerator, with ConsoleReporter and HTMLReporter (implements the Reporter interface) being the modes utilised in `index.ts`.

4. By invoking the `buildAndPrintAnalysisReport` on each instance of ReportGenerator, an analysis will be produced by calling the `run()` method on the analyser with the parsed data, and then by calling the `print()` method on the reporter.

```typescript
const analysers: Analyser<RowItem>[] = [
  new CountAnalyser(),
  new ColumnValueCount('key', 'E'),
  new CountMaxColumnValueReporter(trackHeaders[1]),
]

for (let analyser of analysers) {
  ReportGenerator.forConsole(analyser).buildAndPrintAnalysisReport(tracks)
  ReportGenerator.forHTML(analyser).buildAndPrintAnalysisReport(tracks)
}
```

#### Challenges Addressed:

Analyser classes were instantiated in an array in the order of the challenges, and reports were generated for each analysis:

1. `new CountAnalyser()` - Write a script to identify the number of songs in the file:
2. `new ColumnValueCount('key', 'E')` - Write a script that identify the number of songs in the key of E.
3. `new CountMaxColumnValueReporter(trackHeaders[1])` - Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.

## Environment

### npm

1. Started a project: `npm init -y`
2. Installed dev dependencies: `npm install typescript ts-node nodemon`

### `tsconfig.json`

TypeScript compiler configuration file.  Specified the `rootDir` and `outDir` as follows:

```json
"rootDir": "./src",
"outDir": "./build"
```

### `nodemon.json`

`nodemon` has in-built support [to run TypeScript files with `ts-node`](https://medium.com/@sudarshanadayananda/how-to-live-reload-typescript-node-server-bc40171fdb7).

`nodemon.json` was created for nodemon to execute a single command i.e. `npm start`:

```json
{
  "ignore": ["**/*.test.ts", "**/*.spec.ts", "node_modules"],
  "watch": ["src/**"],
  "exec": "npm start",
  "ext": "ts, json"
}
```

## How to Run

1. Install project dependencies `npm install`.
2. Run CLI scripts found in package.json: `npm run <script name>`

## Scripts

From `package.json`:

```json
  "scripts": {
    "build": "tsc -w",
    "dev": "nodemon",
    "start": "ts-node src/index.ts"
  },
```

The main entry point is `src/index.ts`.

1. `build` - runs TypeScript compiler `tsc` in watch mode to compile TypeScript files into JS files. (Not needed unless not running TS files directly with `ts-node`.)
2. `dev` - runs `nodemon` (in watch mode) for development environment
3. `start` - runs `ts-node` once for production environment
