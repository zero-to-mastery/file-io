import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.HashMap;
import java.util.List;

public class SpotifyDataLogger {
    public static void main(String args[]) {

        CsvReader csvReader;
        try {
            csvReader = new CsvReader("./spotify-2023.csv");
            csvReader.readCSV();
            List<List<String>> spotifyData = csvReader.getCsvData();
            List<String> headers = csvReader.getHeaders();

            DataProcessor spotifyDataProcessor = new DataProcessor(spotifyData, headers);
            HashMap<String, Integer> keyMap = spotifyDataProcessor.countNumberOfKey();

            // Log output
            System.out.println("The total number of songs in the file is: " + spotifyDataProcessor.getNumberOfSongs());
            System.out.println("The total number of songs in the key of E is : " + keyMap.get("E"));
            System.out.println("Total Songs for each key:");
            System.out.println("---------------------------");
            for (String key : keyMap.keySet()) {
                if (!key.isEmpty()) {
                    System.out.println(key + " ---> " + keyMap.get(key));
                }

            }
        } catch (FileNotFoundException e) {
            System.out.println("The file does not exist, please make sure the file name is correct!");
        } catch (IOException e) {
            System.out.println("Cannot read the provided file!");
        } catch (Exception e) {
            System.out.println("Something went wrong, please try again later");
        }

    }

}