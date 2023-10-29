const Papa = require('papaparse');
const fs = require('fs');

const file = fs.readFileSync('spotify-2023.csv', 'utf8');

const handleResultObj = (result) => {
	const csvObj = result;

	const {data} = csvObj;

	showNumberOfSongs(data);

	numOfSongsByKey('E', data);

	countCommonArtist(data);

}

const handleUpload = (event) => {

	const file = event.target.files[0];

	handleParse(file);

}

const showNumberOfSongs = (data) => {
	const numSongs = data.length - 1;

	console.log("Number of Songs:", numSongs);
}

const numOfSongsByKey = (key, data) => {
	const result = data.filter(item => {
		return item['key'] === 'E';
	});

	console.log(`Number of Songs with Key of ${key}:`, result.length);
}

const countCommonArtist = (data) => {

	const artistCounts = {};

	data.forEach((item) => {
	  const artistName = item['artist(s)_name'];
	  if (artistCounts[artistName]) {
	    artistCounts[artistName]++;
	  } else {
	    artistCounts[artistName] = 1;
	  }
	});

	let mostCommonArtist;
	let highestCount = 0;

	for (const artistName in artistCounts) {
	  if (artistCounts[artistName] > highestCount) {
	    mostCommonArtist = artistName;
	    highestCount = artistCounts[artistName];
	  }
	}

	console.log(`The most common artist is "${mostCommonArtist}" with ${highestCount} occurrences.`);
}



Papa.parse(file, {
	header: true,
	delimiter: "",
	newline: "",
	dynamicTyping: true,
	complete: handleResultObj 
});