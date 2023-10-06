import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpotifyAnalysis {
    private static final String KEY = "key";

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Pass in file path to csv");
        }
        final File csv = new File(args[0]);
        if (!csv.exists()) {
            System.out.println("File does not exist.");
            System.exit(3);
        }
        int numberOfSongs = 0;
        int numberOfSongsInKeyOfE = 0;
        final Map<String, Integer> occurrencesOfKey = new HashMap<>();
        try (final BufferedReader reader = new BufferedReader(new FileReader(csv.getAbsolutePath()))) {
            String line = reader.readLine(); // Assuming the first read line is the headers
            final List<String> headers = List.of(line.split(","));
            final int indexOfKey = headers.indexOf(KEY);
            while ((line = reader.readLine()) != null) {
                final String[] row = line.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)");
                numberOfSongs++;
                final String keyOfCurrentSong = row[indexOfKey];
                occurrencesOfKey.merge(keyOfCurrentSong, 1, Integer::sum);
                if (keyOfCurrentSong.equalsIgnoreCase("e")) {
                    numberOfSongsInKeyOfE++;
                }
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
            System.out.println("Failed to parse CSV");
            System.exit(4);
        }

        System.out.println("Total number of songs: " + numberOfSongs);
        System.out.println("Total number of songs in the key of E: " + numberOfSongsInKeyOfE);
        System.out.println("Total Songs for each key:");
        System.out.println("-------------------------------");
        for (Map.Entry<String, Integer> entry : occurrencesOfKey.entrySet()) {
            if (entry.getKey().isEmpty()) {
                System.out.format("%-20s %9d%n", "No Key Available :", entry.getValue());
            } else {
                System.out.format("%-20s %9d%n", entry.getKey(), entry.getValue());
            }
        }
    }
}
