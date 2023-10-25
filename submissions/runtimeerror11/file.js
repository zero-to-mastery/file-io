const csv = require('csv-parser')
const fs = require('fs')

 count1=0//Store the count of total songs
 count2=0//stores the count of songs with key 'E'

//solution for challenge 1 
function fun1(data){
   count1++
}

//solution for challenge 2
function fun2(data){
if(data['key']=='E'){
   count2++
}
}

fs.createReadStream('spotify-2023.csv')
  .pipe(csv())
  .on('data', (data) =>{
    fun1(data)
    fun2(data)
  })
  .on('end', () => {
    console.log("Results-")
    console.log(`Challenge 1 \nTotal Songs = ${count1}`)
    console.log(`Challenge 2 \nSongs with key E = ${count2} `)
    console.log("\nConslusion-")
    console.log(`There are total ${count1} number of songs and ${count2} songs with Key 'E'.\n`)
  });