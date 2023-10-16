const fs = require('fs');
const {parse} = require('csv-parse');

function totalSongCount() {
    let songCount = 0;
    fs.createReadStream('./spotify-2023.csv')
        .pipe(parse({delimiter: ',', from_line: 2}))
        .on('data', (data)=> ++songCount)
        .on('end', (row)=> console.log("Total songs: ", songCount))

}

function songsInECount() {
    let songCount = 0;
    fs.createReadStream('./spotify-2023.csv')
        .pipe(parse({delimiter: ',', from_line: 1, columns: true, group_columns_by_name: true}))
        .on('data', (data)=> {
            if(data.key === "E")
                ++songCount
        })
        .on('end', ()=> console.log("Total songs in E: ", songCount))
}

function artistWithMostSongs() {
    const map = {};
    let currentMax=0
    let mostCommonArtist=""
    fs.createReadStream('./spotify-2023.csv')
        .pipe(parse({delimiter: ',', from_line: 1, columns: true, group_columns_by_name: true}))
        .on('data', (data)=> {
            const current = map[data['artist(s)_name']]
            if(current){
                map[data['artist(s)_name']] = current + 1;
                if(current >= currentMax){
                    mostCommonArtist = data['artist(s)_name']
                    currentMax = current;
                }
            }
            else {
                map[data['artist(s)_name']] = 1
            }
        })
        .on('end', ()=> console.log("Artist with most songs: ", mostCommonArtist))
}

totalSongCount()
songsInECount()
artistWithMostSongs()