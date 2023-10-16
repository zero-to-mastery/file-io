

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class SongCounter {
    public static void main(String[] args) {
        String file = "spotify-2023.csv";
        int songCount = 0; // Initialize the count to 0
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            // Read the file line by line
            while (br.readLine() != null) {
                songCount++;
            }
            System.out.println("Total number of songs: " + songCount);
        } catch (IOException e) {
            // Handle any exceptions that may occur during file reading
            e.printStackTrace();
        }
    }
}
