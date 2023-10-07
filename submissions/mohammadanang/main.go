package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
)

func main() {
	file, err := os.Open("spotify-2023.csv")
	if err != nil {
		log.Fatal("Error while reading the file", err)
	}

	defer file.Close()

	reader := csv.NewReader(file)
	records, err := reader.ReadAll()
	if err != nil {
		log.Fatal("Error reading records", err)
	}

	totalSongs := len(records) - 1
	totalESongs := 0
	var commonArtist string
	var totalCommonArtist int
	dup_artist := make(map[string]int)

	for _, er := range records[1:] {
		if strings.Contains(strings.ToLower(er[0]), "e") {
			totalESongs++
		}

		_, exists := dup_artist[er[1]]
		if exists {
			dup_artist[er[1]] += 1
		} else {
			dup_artist[er[1]] = 1
		}
	}

	keys := make([]string, 0, len(dup_artist))
	for k := range dup_artist {
		keys = append(keys, k)
	}

	sort.SliceStable(keys, func(i, j int) bool {
		return dup_artist[keys[i]] > dup_artist[keys[j]]
	})

	commonArtist = keys[0]
	totalCommonArtist = dup_artist[keys[0]]

	fmt.Println("The number of songs in the file is", totalSongs)
	fmt.Println("The number of songs in the key of E is", totalESongs)
	fmt.Println("The common artist`s name is", commonArtist, "with a total of", totalCommonArtist)
}
