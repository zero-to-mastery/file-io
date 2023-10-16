#![allow(dead_code)]

use std::{env, fmt, fs, process};
use std::collections::HashMap;
use std::fmt::Formatter;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::PathBuf;

#[derive(Eq, Hash, PartialEq, Debug)]
enum Key {
    A,
    ASharp,
    B,
    BSharp,
    C,
    CSharp,
    D,
    DSharp,
    E,
    ESharp,
    F,
    FSharp,
    G,
    GSharp,
    NoKey,
}

impl Key {
    fn get_key(key: &str) -> Self {
        match key {
            "A" => Key::A,
            "A#" => Key::ASharp,
            "B" => Key::B,
            "B#" => Key::BSharp,
            "C" => Key::C,
            "C#" => Key::CSharp,
            "D" => Key::D,
            "D#" => Key::DSharp,
            "E" => Key::E,
            "E#" => Key::ESharp,
            "F" => Key::F,
            "F#" => Key::FSharp,
            "G" => Key::G,
            "G#" => Key::GSharp,
            _ => Key::NoKey,
        }
    }
}

impl fmt::Display for Key {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        let key = match self {
            Key::A => "A".to_owned(),
            Key::ASharp => "A#".to_owned(),
            Key::B => "B".to_owned(),
            Key::BSharp => "B#".to_owned(),
            Key::C => "C".to_owned(),
            Key::CSharp => "C#".to_owned(),
            Key::D => "D".to_owned(),
            Key::DSharp => "D#".to_owned(),
            Key::E => "E".to_owned(),
            Key::ESharp => "E#".to_owned(),
            Key::F => "F".to_owned(),
            Key::FSharp => "F#".to_owned(),
            Key::G => "G".to_owned(),
            Key::GSharp => "G#".to_owned(),
            Key::NoKey => "No Key".to_owned(),
        };
        write!(f, "{}", key)
    }
}

#[derive(Debug)]
struct Data {
    track_name: String,
    artist_name: String,
    artist_count: String,
    released_year: i32,
    released_month: i32,
    released_day: i32,
    in_spotify_playlists: i32,
    in_spotify_charts: i32,
    streams: i64,
    in_apple_playlists: i64,
    in_apple_charts: i32,
    in_deezer_playlists: i32,
    in_deezer_charts: i32,
    in_shazam_charts: String,
    bpm: i32,
    key: Key,
    mode: String,
    danceability: i32,
    valence: i32,
    energy: i32,
    acousticness: i32,
    instrumentalness: i32,
    liveness: i32,
    speechiness: String,
}

impl Data {
    fn create(row: String) -> Self {
        // Loop over string to manually check characters
        let mut data: Vec<String> = Vec::new();
        let mut current_entry = String::new();
        let mut in_quotes = false;

        // Iterate over the string 
        let mut index: usize = 0;
        for c in row.chars() {
            match c {
                // If comma, then push entry into the vector only if the we don't detect 
                // a double quote
                ',' if !in_quotes => {
                    // If the previous and current characters were commas (no data for column)
                    // insert 0
                    let append_zero = match &row.get(index..index) {
                        Some(char) => char.to_string() == ",".to_owned(),
                        None => false
                    };
                    if append_zero {
                        data.push("0".to_string());
                    } else {
                        data.push(current_entry.clone());
                    }
                    current_entry.clear();
                }
                // toggle the double quote flag
                // this tells us if the string is wrapped in a quotes
                '"' => {
                    in_quotes = !in_quotes;
                }
                // append current character to current working string
                _ => {
                    current_entry.push(c);
                }
            }
            index = index + 1;
        }

        // The loop doesn't handle the last column, so we get the index of the last comma
        // and then get the last entry
        let last_index_of_comma = row.rfind(',').unwrap() + 1;
        let last_column = &row[last_index_of_comma..row.len()];

        // Iterator to go through the Vector
        let mut it = data.iter();
        Data {
            track_name: it.next().unwrap().to_string(),
            artist_name: it.next().unwrap().to_string(),
            artist_count: it.next().unwrap().to_string(),
            released_year: it.next().unwrap().parse::<i32>().unwrap(),
            released_month: it.next().unwrap().parse::<i32>().unwrap(),
            released_day: it.next().unwrap().parse::<i32>().unwrap(),
            in_spotify_playlists: it.next().unwrap().parse::<i32>().unwrap(),
            in_spotify_charts: it.next().unwrap().parse::<i32>().unwrap(),
            streams: match it.next().unwrap().parse::<i64>() {
                Ok(num) => num,
                Err(_) => 0
            },
            in_apple_playlists: it.next().unwrap().parse::<i64>().unwrap(),
            in_apple_charts: it.next().unwrap().parse::<i32>().unwrap(),
            in_deezer_playlists: it.next().unwrap().replace(",", "").parse::<i32>().unwrap(),
            in_deezer_charts: it.next().unwrap().parse::<i32>().unwrap(),
            in_shazam_charts: it.next().unwrap().to_string(),
            bpm: it.next().unwrap().parse::<i32>().unwrap(),
            key: Key::get_key(it.next().unwrap()),
            mode: it.next().unwrap().to_string(),
            danceability: it.next().unwrap().parse::<i32>().unwrap(),
            valence: it.next().unwrap().parse::<i32>().unwrap(),
            energy: it.next().unwrap().parse::<i32>().unwrap(),
            acousticness: it.next().unwrap().parse::<i32>().unwrap(),
            instrumentalness: it.next().unwrap().parse::<i32>().unwrap(),
            liveness: it.next().unwrap().parse::<i32>().unwrap(),
            speechiness: last_column.to_string(),
        }
    }
}


fn main() {
    let mut total_songs_in_key: HashMap<Key, i32> = HashMap::new();
    let mut total_songs = 0;
    let mut total_songs_in_e = 0;

    let args: Vec<String> = env::args().collect();
    if args.len() < 2 || args.len() > 3 {
        println!("Too many arguments passed into binary. Only pass in file path to csv");
        process::exit(1);
    }

    let file_path_str = args.get(1).unwrap(); // The path will be the 2nd item in the vector
    let file = match fs::canonicalize(PathBuf::from(&file_path_str)) {
        Ok(path) => path,
        _ => {
            println!("No csv found.");
            process::exit(2);
        }
    };

    let file_data = File::open(file).unwrap();
    let mut reader = BufReader::new(file_data);
    let mut line = String::new();
    reader.read_line(&mut line).unwrap(); // ignore the first line since it's the headers 

    // // Since the CSV contains non-UTF8 character, we need to read it byte by byt
    let mut buf = vec![];
    println!("The following line has invalid encoded characters");
    while let Ok(_) = reader.read_until(b'\n', &mut buf) {
        if buf.is_empty() {
            break;
        }
        // Convert the bytes to a string, including valid UTF8 characters
        let line = String::from_utf8_lossy(&buf);

        // Print lines with invalid characters
        match String::from_utf8(buf.clone()) {
            Err(_) => {
                println!("{}", line)
            }
            _ => {}
        }
        let data = Data::create(line.to_string());
        total_songs += 1;
        match &data.key {
            Key::E => total_songs_in_e += 1,
            _ => ()
        };

        match total_songs_in_key.contains_key(&data.key) {
            true => {
                let mut key_tot = total_songs_in_key.get(&data.key).unwrap().to_owned();
                key_tot += 1;
                total_songs_in_key.insert(data.key, key_tot);
            }
            false => { total_songs_in_key.insert(data.key, 1); }
        }

        buf.clear();
    }

    println!("Total Songs: {}", total_songs);
    println!("Total Songs in key E: {}", total_songs_in_e);
    println!("Total Songs for each key");
    println!("------------------------");
    for (key, total) in total_songs_in_key {
        println!("{0: <20} : {1: <20}", key, total);
    }
}
