import java.io.*;
import java.util.*;

public class Solution {
    private final String [] fields;

    Solution() throws Exception {
        fields = new String[]{"track_name", "artist_name", "artist_count", "released_year", "released_month", "released_day", "in_spotify_playlists", "in_spotify_charts", "streams", "in_apple_playlists", "in_apple_charts", "in_deezer_playlists", "in_deezer_charts", "in_shazam_charts", "bpm", "key", "mode", "danceability", "valence", "energy", "acousticness", "instrumentalness", "liveness", "speechiness"};
    }
    public static void main(String[] args) throws Exception{
        Solution solution = new Solution();
        System.out.println(solution.numberOfSongs()); // 935
        System.out.println(solution.numberOfSongsInKeyOfE()); // 35
        System.out.println(solution.commonValue());
    }
    // Returns a bufferredReader object for processing the CSV file data
    private BufferedReader getBufferedReader() throws Exception{
        FileReader file = new FileReader("../../spotify-2023.csv");
        BufferedReader reader = new BufferedReader(file);
        reader.readLine();
        return reader;
    }
    // Returns total number of songs in the dataset
    private int numberOfSongs() throws Exception{
        BufferedReader reader = getBufferedReader();
        int count = 0;
        while(reader.readLine() != null){
            count += 1;
        }
        return count;
    }
    // Returns the songs that are in the key of E
    private int numberOfSongsInKeyOfE() throws Exception{
        BufferedReader reader = getBufferedReader();
        int count = 0;
        String line = "";
        String [] data;
        while((line = reader.readLine()) != null){
            if(line.split(",")[0].trim().startsWith("E"))
                count += 1;
        }
        return count;
    }
    // Prints the most common value in the specified column
    private String commonValue() throws Exception{
        BufferedReader reader = getBufferedReader();
        HashMap<String, Integer> map = new HashMap<>();
        String line = "";
        String[] data;
        int choice = 0;
        System.out.println("Choose a field:");
        for(int i = 0; i< fields.length; i+=1){
            System.out.println((i+1)+": "+ fields[i]);
        }
        choice = new Scanner(System.in).nextInt() - 1;
        while((line = reader.readLine()) != null){
            data = line.split(",");
            map.put(data[choice], map.getOrDefault(data[choice], 0) + 1);
        }
        return Collections.max(map.keySet());
    }
}
