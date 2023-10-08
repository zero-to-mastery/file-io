# Ruby Spotify Stats Logger

The script is an executable, and you should be able to run it by calling the file name in the directory, as long as ruby is installed on your machine:

```shell
cd submissions/wizbeck21
```
```shell
./spotify_logger
```

You should get an output like:
```shell
Challenge 1: Total songs: 953
Challenge 2: Songs in E Key: 62
```

For challenge three the executable command takes an argument of the column name that you can pass for the script execution in the terminal:
```shell
./spotify_logger key
```
Which gives a list of keys and the number of songs having that key value in the key column:
```
# Output of above command passing 'key'
Challenge 1: Total songs found: 953
Challenge 2: Songs in key 'E': 62
{"B"=>81, "C#"=>120, "F"=>89, "A"=>75, "D"=>81, "F#"=>73, nil=>95, "G#"=>91, "G"=>96, "E"=>62, "A#"=>57, "D#"=>33}
```