package main

import (
	"encoding/csv"
	"fmt"
	"os"
)

func main() {

	// Open csv file
	file, err := os.Open("spotify-2023.csv")
	if err != nil {
		fmt.Println("Error opening csv file:", err)
		return
	}
	defer file.Close()

	// Create a new csv reader and read the entire contents of the file
	reader := csv.NewReader(file)
	songData, err := reader.ReadAll()

	// First row is the header, so we minus that to get the amount of songs
	amtOfSongs := len(songData) - 1
	fmt.Println(amtOfSongs)

	fmt.Println(countSongsInKey(songData, "A"))
	fmt.Println(countMostOccurencesInColumn(songData, "artist(s)_name"))
}

func getRequestedColumn(data [][]string, columnRequest string) int {
	for i := 0; i < len(data); i++ {
		// data[0] represents the headers, we iterate through the header to find the 'key' column
		if data[0][i] == columnRequest {
			return i
		}
	}
	return -1
}

// Function accepts the songdata, the key whose occurences you wish to count
func countSongsInKey(data [][]string, key string) int {
	keyColumn := getRequestedColumn(data, "key")
	amtSongsInKey := 0
	for i := 1; i < len(data); i++ {
		if data[i][keyColumn] == key {
			amtSongsInKey++
		}
	}
	return amtSongsInKey
}

func countMostOccurencesInColumn(data [][]string, columnToCount string) string {
	cache := mapAllOccurences(data, columnToCount)
	maxOccurences := 0
	var retValue string
	for key := range cache {
		if cache[key] > maxOccurences {
			maxOccurences = cache[key]
			retValue = key
		}
	}
	return retValue
}

func mapAllOccurences(data [][]string, columnToCount string) map[string]int {
	columnIndex := getRequestedColumn(data, columnToCount)
	cache := make(map[string]int)
	for i := 1; i < len(data); i++ {
		currentValue := data[i][columnIndex]
		_, exists := cache[currentValue]
		if exists {
			cache[currentValue]++
		} else {
			cache[currentValue] = 0
		}
	}
	return cache
}
