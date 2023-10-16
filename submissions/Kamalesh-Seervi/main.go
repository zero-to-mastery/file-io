package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
)

func main() {
	// Open the CSV file
	file, err := os.Open("spotify-2023.csv")
	if err != nil {
		log.Fatalf("Error opening CSV file: %v", err)
	}
	defer file.Close()

	// Create a CSV reader
	csvReader := csv.NewReader(file)

	// Read all lines from the CSV file
	lines, err := csvReader.ReadAll()
	if err != nil {
		log.Fatalf("Error reading CSV: %v", err)
	}

	// Calculate the number of songs (excluding the header)
	numSongs := len(lines) - 1

	fmt.Printf("Number of songs in the file: %d\n", numSongs)

}
