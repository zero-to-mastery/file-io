package submissions.stephenteay;

import java.io.*;
import java.util.*;

public class SpotifyDataLoggerSubmission {

    private static final int READ_LIMIT = 140 * 1024;
    private static final BufferedReader csvReader;
    private static final String headerLine;

    static {
        try {
            csvReader = new BufferedReader(new FileReader("spotify-2023.csv"));
            headerLine = csvReader.readLine();
            csvReader.mark(READ_LIMIT);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static int getSongCount() throws IOException {
        csvReader.reset();
        int songColumnIndex = getHeaderIndex("track_name");
        int songCount = 0;
        String line;
        while ((line = csvReader.readLine()) != null) {
            String[] values = line.split(",");
            if (values.length > songColumnIndex && !values[songColumnIndex].trim().isEmpty()) {
                songCount++;
            }
        }
        return songCount;
    }

    public static int getSongCountByKey(String key) throws IOException {
        csvReader.reset();
        int keyColumnIndex = getHeaderIndex("key");
        int songCountByKey = 0;
        String line;
        while ((line = csvReader.readLine()) != null) {
            String[] values = line.split(",");
            if (values.length > keyColumnIndex && values[keyColumnIndex].trim().equalsIgnoreCase(key)) {
                songCountByKey++;
            }
        }
        return songCountByKey;
    }

    public static ArrayList<String> getValuesPerColumn(String columnName) throws IOException {
        csvReader.reset();
        String maxEntryName = null;
        ArrayList<String> result = new ArrayList<>();
        int columnIndex = getHeaderIndex(columnName);
        int count = 0;
        String line;
        ArrayList<String> columnValues = new ArrayList<>();
        Map<String, Integer> counts = new HashMap<>();

        while ((line = csvReader.readLine()) != null) {
            String[] values = line.split(",");
            if (values.length > columnIndex && !values[columnIndex].trim().isEmpty()) {
                columnValues.add(Arrays.toString(values));
                count++;
            }

            if (!columnValues.isEmpty()) {
                for (String value : columnValues) {
                    counts.put(value, counts.getOrDefault(value, 0) + 1);
                }
                 String maxEntry = counts.entrySet().stream()
                        .max(Map.Entry.comparingByValue())
                        .map(Map.Entry::getKey)
                        .orElse("");
                maxEntryName = maxEntry.split(",")[0];
            }

        }
        result.add(String.valueOf(count));
        result.add(maxEntryName);

        return result;
    }

    public static int getHeaderIndex(String header) {
        if (headerLine != null) {
            List<String> headers = Arrays.asList(headerLine.split(","));
            int index = headers.indexOf(header);
            if (index == -1) throw new RuntimeException("Column not found: " + header);
            return index;
        }
        throw new RuntimeException("Malformed File");
    }

    public static void main(String[] args) throws IOException {
        System.out.println(getSongCountByKey("E"));
        System.out.println(getSongCount());
        System.out.println(getValuesPerColumn("released_month"));
    }
}