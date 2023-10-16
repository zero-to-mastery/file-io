package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
)

const (
	artistNameHeader = "artist(s)_name"
	keyHeader        = "key"
)

type Song struct {
	ArtistName string
	Key        string
}

func main() {
	filePath := "spotify-2023.csv"
	songs, err := readCSVFile(filePath)
	if err != nil {
		log.Fatalf("Error reading CSV file: %v", err)
	}

	numberOfSongs := len(songs)
	numberOfKeyOfESongs := countKeyOfESongs(songs)
	artistNameOccurrences := countArtistNameOccurrences(songs)

	mostCommonArtist, mostCommonArtistOccurrences := findMostCommonArtist(artistNameOccurrences)

	fmt.Printf("🎶 Total number of songs: %d\n", numberOfSongs)
	fmt.Printf("🎹 Number of songs in the key of E: %d\n", numberOfKeyOfESongs)
	fmt.Printf("👸 Most common artist: %s (%d songs)\n", mostCommonArtist, mostCommonArtistOccurrences)
}

func readCSVFile(filePath string) ([]Song, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	reader := csv.NewReader(file)
	records, err := reader.ReadAll()
	if err != nil {
		return nil, err
	}

	var songs []Song
	for i := 1; i < len(records); i++ {
		song := Song{
			ArtistName: records[i][findHeaderIndex(records[0], artistNameHeader)],
			Key:        records[i][findHeaderIndex(records[0], keyHeader)],
		}
		songs = append(songs, song)
	}

	return songs, nil
}

func findHeaderIndex(headers []string, headerName string) int {
	for i, header := range headers {
		if header == headerName {
			return i
		}
	}
	return -1
}

func countKeyOfESongs(songs []Song) int {
	count := 0
	for _, song := range songs {
		if song.Key == "E" {
			count++
		}
	}
	return count
}

func countArtistNameOccurrences(songs []Song) map[string]int {
	occurrences := make(map[string]int)
	for _, song := range songs {
		occurrences[song.ArtistName]++
	}
	return occurrences
}

func findMostCommonArtist(occurrences map[string]int) (string, int) {
	var mostCommonArtist string
	var mostOccurrences int
	for artist, count := range occurrences {
		if count > mostOccurrences {
			mostCommonArtist = artist
			mostOccurrences = count
		}
	}
	return mostCommonArtist, mostOccurrences
}
