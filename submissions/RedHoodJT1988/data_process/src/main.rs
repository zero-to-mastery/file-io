use std::collections::HashMap;
use std::env;
use std::error::Error;
use std::fs;
use std::fs::File;
use std::path::PathBuf;
use std::process;

fn main() -> Result<(), Box<dyn Error>> {
    let mut total_songs_in_key: HashMap<String, i32> = HashMap::new();
    let mut total_songs = 0;
    let mut total_songs_in_e = 0;

    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage: cargo run <file path to csv>");
        process::exit(1);
    }

    let file_path_str = &args[1];
    let file = fs::canonicalize(PathBuf::from(&file_path_str))?;
    let file_data = File::open(&file)?;

    let mut csv_rdr = csv::Reader::from_reader(file_data);
    for row in csv_rdr.records() {
        let data = match row {
            Ok(data) => data,
            Err(_) => {
                eprintln!("Error reading row data.");
                process::exit(4);
            }
        };

        total_songs += 1;

        let key = data.get(15).unwrap_or_default().to_lowercase();
        if key == "e" {
            total_songs_in_e += 1;
        }

        *total_songs_in_key.entry(key.to_owned()).or_insert(0) += 1;
    }

    println!("Total Songs: {}", total_songs);
    println!("Total Songs in key E: {}", total_songs_in_e);
    println!("Total Songs in each key:");

    let mut no_key_total = 0;
    println!("--------------------");
    for (key, total) in &total_songs_in_key {
        if !key.is_empty() {
            println!("{0: <10} : {1: <10}", key, total);
        } else {
            no_key_total = *total;
        }
    }
    println!("{0: <10} : {1: <10}", "No Key", no_key_total);

    Ok(())
}
