use csv;
use std::collections::HashMap;
use std::env;
use std::error::Error;
use std::fs::File;
use std::process;

fn err(msg: &str) {
    eprintln!("{}", msg);
    process::exit(1);
}

fn load_csv(path: &str) -> Result<csv::Reader<File>, Box<dyn Error>> {
    let file = File::open(path)?;
    let rdr = csv::Reader::from_reader(file);
    Ok(rdr)
}

struct Challenge {
    data: csv::Reader<File>,
    functions: Vec<Box<dyn FnMut(csv::StringRecord, Option<Box<dyn FnMut(i32) -> i32>>) -> Option<Box<dyn FnMut(i32) -> i32>>>,
        result: Vec<Option<i32>>,
        state: HashMap<usize, Option<Box<dyn FnMut(i32) -> i32>>>,
}

impl Challenge {
    fn new(data: csv::Reader<File>) -> Self {
        Challenge {
            data,
            functions: Vec::new(),
            result: Vec::new(),
            state: HashMap::new(),
        }
    }

    fn song_count(&mut self) -> &mut Self {
        self.functions.push(Box::new(|record, accumulator| match accumulator {
            Some(mut acc) => {
                if record["track_name"].is_empty() {
                    acc(0)
                } else {
                    acc(1)
                }
                Some(acc)
            }
            None => {
                let mut acc = Box::new(|a| a) as Box<dyn FnMut(i32) -> i32>;
                if record["track_name"].is_empty() {
                    acc(0)
                } else {
                    acc(1)
                }
                Some(acc)
            }
        });
        self
    }

    fn song_count_by_key(&mut self, key: &str) -> &mut Self {
        self.functions.push(Box::new(move |record, accumulator| match accumulator {
            Some(mut acc) => {
                if record["key"] == key {
                    acc(1)
                } else {
                    acc(0)
                }
                Some(acc)
            }
            None => {
                let mut acc = Box::new(|a| a) as Box<dyn FnMut(i32) -> i32>;
                if record["key"] == key {
                    acc(1)
                } else {
                    acc(0)
                }
                Some(acc)
            }
        });
        self
    }

    fn most_common_element_by_column(&mut self, col: &str) -> &mut Self {
        self.functions.push(Box::new(|record, accumulator| match accumulator {
            Some(mut acc) => {
                let mut map = HashMap::new();
                if let Some(value) = record.get(col) {
                    *map.entry(value).or_insert(0) += 1;
                }
                acc(map.into_iter().max_by_key(|&(_, count)| count).map(|(k, _)| k))
            }
            None => {
                let mut acc = Box::new(|a| a) as Box<dyn FnMut(i32) -> i32>;
                let mut map = HashMap::new();
                if let Some(value) = record.get(col) {
                    *map.entry(value).or_insert(0) += 1;
                }
                acc(map.into_iter().max_by_key(|&(_, count)| count).map(|(k, _)| k))
            }
        });
        self
    }

    fn result(&mut self) -> Vec<i32> {
        for f in &mut self.functions {
            self.state.insert(f as *mut _ as usize, f(0, self.state.get_mut(&(f as *mut _ as usize)));
        }

        for result in self.data.records() {
            if let Ok(record) = result {
                for f in &mut self.functions {
                    self.state.insert(f as *mut _ as usize, f(record.clone(), self.state.get_mut(&(f as *mut _ as usize)));
                }
            }
        }

        for f in &mut self.functions {
            if let Some(acc) = self.state.get_mut(&(f as *mut _ as usize)) {
                self.result.push(Some(acc(0)));
            } else {
                self.result.push(None);
            }
        }

        self.result
            .iter()
            .map(|x| x.map_or(0, |f| f))
            .collect()
    }
}

fn process_csv(path: &str) -> Result<Vec<i32>, Box<dyn Error>> {
    if !(path.ends_with(".csv") && std::path::Path::new(path).exists()) {
        eprintln!("Warning: provided file path is invalid");
        eprintln!("Picking CSV file from script's parent directory...");
        let path = "./spotify-2023.csv";
        let data = load_csv(path)?;

        let results = Challenge::new(data)
            .song_count()
            .song_count_by_key("E")
            .song_count_by_key("D")
            .most_common_element_by_column("bpm")
            .most_common_element_by_column("track_name")
            .result();

        Ok(results)
    } else {
        Err("Invalid file path".into())
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        err("Usage: cargo run <file path>");
    }

    let path = &args[1];
    let results = process_csv(path)?;

    println!(
        "Total Songs found in data: {}\nTotal Songs by key \"E\": {}\nTotal Songs by key \"D\": {}\nMost Common Element by Col \"bpm\": {:?}\nMost Common Element by Col \"track_name\": {:?}",
        results[0], results[1], results[2], results[3], results[4]
    );

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_song_count() {
        let input = csv::Reader::from_reader("track_name,key\nSong1,E\nSong2,D\nSong3,E\n");
        let mut challenge = Challenge::new(input);
        let results = challenge.song_count().result();
        assert_eq!(results[0], 3);
    }

    #[test]
    fn test_song_count_by_key() {
        let input = csv::Reader::from_reader("track_name,key\nSong1,E\nSong2,D\nSong3,E\n");
        let mut challenge = Challenge::new(input);
        let results = challenge.song_count_by_key("E").song_count_by_key("D").result();
        assert_eq!(results[1], 2);
        assert_eq!(results[2], 1);
    }

    #[test]
    fn test_most_common_element_by_column() {
        let input = csv::Reader::from_reader("track_name,bpm\nSong1,120\nSong2,140\nSong3,120\n");
        let mut challenge = Challenge::new(input);
        let results = challenge.most_common_element_by_column("bpm").result();
        assert_eq!(results[3], Some("120".to_string()));
    }

    #[test]
    fn test_integration() {
        let input = csv::Reader::from_reader("track_name,key,bpm\nSong1,E,120\nSong2,D,140\nSong3,E,120\n");
        let mut challenge = Challenge::new(input);
        let results = challenge
            .song_count()
            .song_count_by_key("E")
            .song_count_by_key("D")
            .most_common_element_by_column("bpm")
            .result();
        assert_eq!(results[0], 3);
        assert_eq!(results[1], 2);
        assert_eq!(results[2], 1);
        assert_eq!(results[3], Some("120".to_string()));
    }
}
