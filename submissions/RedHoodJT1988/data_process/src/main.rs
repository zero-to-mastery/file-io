extern crate csv;

use std::collections::HashMap;
use std::error::Error;
use std::fs::File;

fn main() -> Result<(), Box<dyn Error>> {
    let file_path = "../../spotify-2023.csv";

    let file = File::open(file_path)?;

    // Create a CSV reader
    let mut rdr = csv::Reader::from_reader(file);

    // Task 1: Number of songs in the file
    let num_songs = rdr.records().count();

    // Reopen the CSV file to create a new reader
    let file = File::open(file_path)?;
    let mut rdr = csv::Reader::from_reader(file);

    // Task 2: Number of songs in the key of E
    let num_songs_in_key_e = rdr
        .records()
        .filter_map(|record| record.ok())
        .filter(|record| record.get("key") == Some("E"))
        .count();

    // Reopen the CSV file to create a new reader
    let file = File::open(file_path)?;
    let rdr = csv::Reader::from_reader(file);

    // Task 3: Count occurrences of artist name(s) and determine the most common value
    let mut artist_counts = HashMap::new();

    for result in rdr.records() {
        let record = result?;
        if let Some(artist) = record.get("artist(s)_name") {
            *artist_counts.entry(artist.to_string()).or_insert(0) += 1;
        }
    }

    let (most_common_artist, most_common_artist_count) = artist_counts
        .iter()
        .max_by_key(|&(_, count)| count)
        .unwrap();

    // Outputs
    println!("Total number of songs in the file: {}", num_songs);
    println!("Number of songs in the key of E: {}", num_songs_in_key_e);
    println!(
        "Most common artist: {}, Occurrences: {}",
        most_common_artist, most_common_artist_count
    );

    Ok(())
}
