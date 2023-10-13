const fs = require('fs');
const fastCsv = require('fast-csv');

const count = {} //for counting all artist occurrances

fs.createReadStream('spotify-2023.csv')
.pipe(fastCsv.parse({headers : true}))
.on('data' , (row) => {
    const artist = row['artist(s)_name'];

    if(count[artist]){    //count logic
        count[artist]++;  
    }else{
        count[artist] = 1; 
    }
})
.on('end' , () => {

    //for counting most occurred
    let mostOccurredArtist = null;  
    let mostOccurredCount = 0;

    for (const artist in count) {  //count logic
      if (count[artist] > mostOccurredCount) {
        mostOccurredArtist = artist;
        mostOccurredCount = count[artist];
      }
    }


    //display output 
    console.log('Counts:');    
    for (const artistName in count) {
      console.log(`${artistName}: ${count[artistName]}`);
    }

    console.log(`Most Occurred Artist: ${mostOccurredArtist}`);
    console.log(`Count: ${mostOccurredCount}`);
})

