package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
)

func main() {
	file, err := os.Open("spotify-2023.csv")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	reader := csv.NewReader(file)

	records, err := reader.ReadAll()
	if err != nil {
		log.Fatal(err)
	}

	totalSongs := len(records) - 1

	songsInKeyE := 0
	keyIndex := getColumnIndex("key", records[0])
	for _, record := range records[1:] {
		if record[keyIndex] == "E" {
			songsInKeyE++
		}
	}

	artistNameIndex := getColumnIndex("artist(s)_name", records[0])
	artistCount := make(map[string]int)
	for _, record := range records[1:] {
		artistName := record[artistNameIndex]
		artistCount[artistName]++
	}

	mostCommonArtist := ""
	maxCount := 0
	for artistName, count := range artistCount {
		if count > maxCount {
			mostCommonArtist = artistName
			maxCount = count
		}
	}

	fmt.Printf("Total songs: %d\n", totalSongs)
	fmt.Printf("Songs in the key of E: %d\n", songsInKeyE)
	fmt.Printf("Most common artist: %s\n", mostCommonArtist)

}

// Helper functions
func getColumnIndex(columnName string, headerRow []string) int {
	for i, column := range headerRow {
		if column == columnName {
			return i
		}
	}
	return -1
}
