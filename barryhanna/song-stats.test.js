const { parse } = require('csv-parse/sync');
const {
	getNumberOfSongs,
	getNumberOfSongsInKey,
	getMostPopularArtist,
} = require('./song-stats.js');

const TEST_DATA_RAW = `track_name,artist(s)_name,artist_count,released_year,released_month,released_day,in_spotify_playlists,in_spotify_charts,streams,in_apple_playlists,in_apple_charts,in_deezer_playlists,in_deezer_charts,in_shazam_charts,bpm,key,mode,danceability_%,valence_%,energy_%,acousticness_%,instrumentalness_%,liveness_%,speechiness_%
Seven (feat. Latto) (Explicit Ver.),"Latto, Jung Kook",2,2023,7,14,553,147,141381703,43,263,45,10,826,125,B,Major,80,89,83,31,0,8,4
LALA,Myke Towers,1,2023,3,23,1474,48,133716286,48,126,58,14,382,92,C#,Major,71,61,74,7,0,10,4
vampire,Olivia Rodrigo,1,2023,6,30,1397,113,140003974,94,207,91,14,949,138,F,Major,51,32,53,17,0,31,6
Cruel Summer,Taylor Swift,1,2019,8,23,7858,100,800840817,116,207,125,12,548,170,A,Major,55,58,72,11,0,11,15
Cruel Summer,Taylor Swift,1,2019,8,23,7858,100,800840817,116,207,125,12,548,170,A,Major,55,58,72,11,0,11,15`;

const TEST_DATA_PARSED = parse(TEST_DATA_RAW, {
	columns: true,
	skip_empty_lines: true,
});

test('total number of songs to be 5', () => {
	expect(getNumberOfSongs(TEST_DATA_PARSED)).toBe(5);
});

test('total number of songs in key of A to be 2', () => {
	expect(getNumberOfSongsInKey(TEST_DATA_PARSED, 'A')).toBe(2);
});

test('most popular artist to be Taylor Swift with 2 songs', () => {
	const mostPopularArtist = getMostPopularArtist(
		TEST_DATA_PARSED,
		'artist(s)_name'
	);
	expect(mostPopularArtist.artist).toBe('Taylor Swift');
	expect(mostPopularArtist.songs).toBe(2);
});
