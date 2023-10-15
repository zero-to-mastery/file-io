import analyzer.RecordsAnalyzer;
import org.apache.commons.csv.CSVRecord;
import parser.CSVFileParser;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.List;
import java.util.Map;

public class CSVAnalyzer {
    private static final String CSV_FILE = "file-io-java-maven/src/spotify-2023.csv";
    public static void main(String[] args) {
        try {
            File file = new File(CSV_FILE);
            CSVFileParser parser = new CSVFileParser();
            parser.parseCsv(file); // Parse CSV File
            List<String> headers = parser.getHeaders(); // Get headers
            List<CSVRecord> csvRecords = parser.getRecords(); // Get records
            RecordsAnalyzer recordsAnalyzer = new RecordsAnalyzer(headers, csvRecords); // Analyse records and perform operations
            System.out.println("Total number of songs in the file = "
                    + recordsAnalyzer.getNumberOfSongsInTheFile());
            System.out.println("Number of songs with key E = "
                    + recordsAnalyzer.getValuesCountForKey("key", "E"));
            System.out.println("Maximum occurrences from each column = ");
            Map<String, String> maxValuesForColumn = recordsAnalyzer.getMaxValuesForColumn();
            for(Map.Entry<String, String> entry: maxValuesForColumn.entrySet()) {
                System.out.println(entry.getKey() + " " + entry.getValue());
            }
        } catch (FileNotFoundException fileNotFoundException) {
            System.out.println("File not found. Please provide valid file");
        } catch (IOException ioException) {
            System.out.println("Error in reading CSV File");
        } catch (Exception e) {
            System.out.println("Sorry something went wrong. Please try again later");
        }
    }
}
