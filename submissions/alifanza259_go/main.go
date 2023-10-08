package main

import (
	"bytes"
	"encoding/csv"
	"fmt"
	"io/fs"
	"log"
	"os"
)

var (
	ArtistName = "artist(s)_name"
	Key        = "key"
)

func main() {
	file, err := fs.ReadFile(os.DirFS("."), "spotify-2023.csv")
	if err != nil {
		log.Fatal(err)
	}

	csv := csv.NewReader(bytes.NewBuffer(file))
	rows, err := csv.ReadAll()
	if err != nil {
		log.Fatal(err)
	}

	var artistNameIndex *int
	var keyIndex *int

	// Map header index
	headerRow := rows[0]
	for i := 0; i < len(headerRow); i++ {
		if headerRow[i] == ArtistName {
			artistNameIndex = new(int)
			*artistNameIndex = i
		}
		if headerRow[i] == "key" {
			keyIndex = new(int)
			*keyIndex = i
		}
	}

	// Exit program if header is not present in file
	if artistNameIndex == nil || keyIndex == nil {
		log.Fatal("One of the headers is not present in file")
	}

	// Prepare answer variables
	numberOfSongs := 0
	numberOfKeyOfESongs := 0
	artistNameOccurences := map[string]int{}

	// Start from 1 to skip header
	for i := 1; i < len(rows); i++ {
		row := rows[i]
		numberOfSongs++

		key := row[*keyIndex]
		if key == "E" {
			numberOfKeyOfESongs++
		}

		artistName := row[*artistNameIndex]

		if _, ok := artistNameOccurences[artistName]; !ok {
			artistNameOccurences[artistName] = 1
		} else {
			artistNameOccurences[artistName]++
		}
	}

	// Find most common artist name value
	mostCommonArtist := ""
	mostCommonArtistOccurence := 0

	for key, val := range artistNameOccurences {
		if val > mostCommonArtistOccurence {
			mostCommonArtist = key
			mostCommonArtistOccurence = val
		}
	}

	fmt.Println("Number of songs in the file: ", numberOfSongs)
	fmt.Println("Number of songs in the key of E: ", numberOfKeyOfESongs)
	fmt.Println("Most common value for column artists_name: ", mostCommonArtist)
}
