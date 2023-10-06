package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
)

// Define the main function
func main() {
	// Open the csv file
	file, err := os.Open("spotify-2023.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Create a csv reader
	reader := csv.NewReader(file)

	// Read all the records
	records, err := reader.ReadAll()
	if err != nil {
		log.Fatal(err)
	}
	var columns = records[0]
	records = records[1:]

	var songsCount = len(records)
	var indexOfKeyE = -1
	var indexOfArtistName = -1

	var artistFrequency = make(map[string]int)

	for i, x := range columns {
		if x == "key" {
			indexOfKeyE = i
		}
		if x == "artist(s)_name" {
			indexOfArtistName = i
		}
	}

	var songsInKeyOfECount = 0

	for _, record := range records {
		var artistName = ""
		if len(record[indexOfArtistName]) > 0 {
			artistName = record[indexOfArtistName]
		}

		artistFrequency[artistName]++

		if record[indexOfKeyE] == "E" {
			songsInKeyOfECount++
		}
	}

	var mostPopularSinger = ""
	var popularSingerSongsCount = 0

	for singer, f := range artistFrequency {
		if f > popularSingerSongsCount {
			mostPopularSinger = singer
			popularSingerSongsCount = f
		}
	}

	fmt.Printf("There are %d songs in this list.\n", songsCount)
	fmt.Printf("There are %d songs in the key of E.\n", songsInKeyOfECount)
	fmt.Printf("The most popular artist is %s with %d songs.", mostPopularSinger, popularSingerSongsCount)
}
