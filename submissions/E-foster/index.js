// Author: Eric Foster
// Submission: Hacktoberfest

// Main Menu (Console Menu)
const mainMenu = () => {
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    console.log("What action would you like to take? Please type a number that corresponds with your desired action and hit enter.")
    console.log("1: Read all content within the spotify CSV file.")
    console.log("2: Retrieve the number of songs within the file.")
    console.log("3: Retrieve the number of songs in the key of E.")
    console.log("4: Exit this program.")
    readline.question("Type a Number: ", (action) => {
        switch (action) {
            case "1":
                readCsv();
                break;

            case "2":
                amountOfSongs()
                break;

            case "3":
                numSongsKeyE();
                break;

            case "4":
                readline.close();
                break;
        }
        readline.close();
    });
}

mainMenu();

// Global Variables
const fs = require("fs");
const { parse } = require("csv-parse");

// Script to read and show all values in the csv file
const readCsv = () => {
    const data = []

    fs.createReadStream("./spotify-2023.csv")
        .pipe(
            parse({
            delimiter: ",",
            columns: true,
            ltrim: true,
            })
        )
        .on("data", function (row) {
            // This will push the object row into the array
            data.push(row);
        })
        .on("error", function (error) {
            console.log(error.message);
        })
        .on("end", function () {
            // Here log the result array
            console.log("parsed csv data:");
            console.log(data);
            console.log("");
            mainMenu();
        });

}

// Script for the amount of songs in the file
const amountOfSongs = () => {
    let numOfSongs = 0
    const data = []

    fs.createReadStream("./spotify-2023.csv")
        .pipe(
            parse({
            delimiter: ",",
            columns: true,
            ltrim: true,
            })
        )
        .on("data", function (row) {
            // This will push the object row into the array
            data.push(row);
        })
        .on("error", function (error) {
            console.log(error.message);
        })
        .on("end", function () {
            // Here log the result array
            songNum();
            console.log("");
            mainMenu();
        });

    const songNum = () => {
        for (let i = 0; i < data.length; i++) {
            numOfSongs++;
        }
        console.log(`The number of songs found in this file is ${numOfSongs}.`);
    }
}

// Script for the amount of songs in key of E
const numSongsKeyE = () => {
    let numOfSongs = 0
    const data = []
    
    fs.createReadStream("./spotify-2023.csv")
        .pipe(
            parse({
            delimiter: ",",
            columns: true,
            ltrim: true,
            })
        )
        .on("data", function (row) {
            // This will push the object row into the array
            data.push(row);
        })
        .on("error", function (error) {
            console.log(error.message);
        })
        .on("end", function () {
            // Here log the result array
            keyOfEList();
            console.log("");
            mainMenu();
        });
    
    const keyOfEList = () => {
        for (let i = 0; i < data.length; i++) {
            if (data[i].key === "E") {
                numOfSongs++;
            }
        }
        console.log(`The number of songs found in the key of E in this file is ${numOfSongs}.`);
    }
}

// I chose not to implement the third and final challenge.