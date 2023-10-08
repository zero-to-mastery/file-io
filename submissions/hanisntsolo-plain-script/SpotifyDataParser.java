
import java.util.Map;
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.UUID;

public class SpotifyDataParser {
	/*
	### Challenges
	1. Write a script to identify the number of songs in the file.
	2. Write a script that identify the number of songs in the key of E.
	3. Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.
	*/
    
    //To make print faster
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {

        processCSV();

        out.flush(); // to flush the output
    }
    public static void processCSV() throws IOException {
        //Need to load csv Data first
        Map<UUID, List<String>> csvData = loadCsVData();
        //Task1.
        // identifyNumberOfSongsInTheFile();
        out.print( "NumberOfSongsInTheFile-:: " + csvData.size() + "\n\n");
        //Task2.
        // identifyNumberOfSongsInTheFileWithKeyOfE(String key);
        out.print( "NumberOfSongsInTheFileWithKeyOfE-:: " + identifyNumberOfSongsInTheFileWithKeyOfE("125", 14, csvData) + "\n\n");		
        //Task3.
        // countTheOccurencesOfValuesInASpecifiedColumn(String columnName);
        out.print( "TheOccurencesOfValuesInASpecifiedColumn-:: " + countTheOccurencesOfValuesInASpecifiedColumn("125", 14, "bpm", csvData) + "\n");

    }

    public static Map<UUID, List<String>> loadCsVData() throws IOException {
    	
    	return loadCSVIntoHashMap("spotify-2023.csv");

    }
    public static Map<UUID, List<String>> loadCSVIntoHashMap(String filePath) throws IOException {
        
        Map<UUID, List<String>> dataMap = new HashMap<>();
        int keyCount = 0;
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            dataMap = br.lines()
                    .map(line -> line.split(",")) // Assuming CSV fields are comma-separated
                    .collect(Collectors.toMap(
                            columns -> UUID.randomUUID(),    // Assuming the first column is the key
                            columns -> {
                                List<String> values = new ArrayList<>();
                                for (int i = 0; i < columns.length; i++) {
                                    values.add(columns[i]);
                                }
                                return values;
                            },
                            (existingValue, newValue) -> existingValue
                    ));
        }

        return dataMap;
    }
    public static int identifyNumberOfSongsInTheFileWithKeyOfE(String key, int columnIndex, Map<UUID, List<String>> dataMap) {

    	int count = 0;		
        
        for (List<String> values : dataMap.values()) {
            if (columnIndex < values.size() && values.get(columnIndex).equals(key)) {
                count++;
            }
        }

        return count;
    }
    public static int countTheOccurencesOfValuesInASpecifiedColumn(String key, int columnIndex, String val, Map<UUID, List<String>> dataMap) {

    	Map<String, Integer> valueCountMap = new HashMap<>();

        for (List<String> values : dataMap.values()) {
            if (columnIndex < values.size()) {
                String value = values.get(columnIndex).trim(); // Get the value from the specified column

                // Update the count in the HashMap
                valueCountMap.put(value, valueCountMap.getOrDefault(value, 0) + 1);
            }
        }

        return valueCountMap.get(val);
    }


}