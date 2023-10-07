use std::{
    collections::HashMap,
    env,
    fs::{self, File},
    path::PathBuf,
    process,
};

fn main() {
    let mut total_songs_in_key: HashMap<String, i32> = HashMap::new();
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


    let mut csv_rdr = csv::Reader::from_reader(file_data);
    for row in csv_rdr.records() {
        let data = match row {
            Ok(data) => {
                total_songs += 1;
                data
            }
            _ => process::exit(4), // If no row data, then exit with error
        };

        let key = &data.get(15).unwrap().to_owned();
        if &key.to_lowercase() == "e" {
            total_songs_in_e += 1;
        }

        if total_songs_in_key.contains_key(key) {
            let mut key_tot = total_songs_in_key.get(key).unwrap().to_owned();
            key_tot += 1;
            total_songs_in_key.insert(key.to_owned(), key_tot);
        } else {
            total_songs_in_key.insert(key.to_owned(), 1);
        }
    }

    println!("Total Songs: {}", total_songs);
    println!("Total Songs in key E: {}", total_songs_in_e);
    println!("Total Songs in each key:");

    let mut no_key_total = 0;
    println!("------------------------");
    for (key, total) in total_songs_in_key {
        if key != "" {
            println!("{0: <10} : {1: <10}", key, total);
        } else {
            no_key_total = total
        };
    }
    println!("{0: <10} : {1: <10}", "No Key", no_key_total);
}
