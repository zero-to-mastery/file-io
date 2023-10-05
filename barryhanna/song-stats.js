const getNumberOfSongs = (songData) => songData.length;

const getNumberOfSongsInKey = (songData, key) =>
	songData.filter((song) => song.key === key).length;

const getMostPopularArtist = (songData, columnName) => {
	const sortedArtistsWithSongTotal = Object.entries(
		songData.reduce((acc, val) => {
			const artistName = val[columnName];
			if (!acc[artistName]) {
				acc[artistName] = 1;
			} else {
				acc[artistName] += 1;
			}
			return acc;
		}, {})
	).sort((a, b) => b[1] - a[1]);
	return {
		artist: sortedArtistsWithSongTotal[0][0],
		songs: sortedArtistsWithSongTotal[0][1],
	};
};

module.exports = {
	getNumberOfSongs,
	getNumberOfSongsInKey,
	getMostPopularArtist,
};
