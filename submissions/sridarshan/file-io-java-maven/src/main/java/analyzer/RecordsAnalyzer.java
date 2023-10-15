package analyzer;

import org.apache.commons.csv.CSVRecord;

import java.util.*;

public class RecordsAnalyzer {

    private final Map<String, Map<String, Integer>> columnVsValuesCount;
    private final List<CSVRecord> csvRecords;
    private final List<String> headers;

    public RecordsAnalyzer (List<String> headers, List<CSVRecord> records) {
        this.csvRecords = records;
        this.headers = headers;
        this.columnVsValuesCount = new HashMap<>();
        init(headers, records);
    }

    private void init(List<String> headers, List<CSVRecord> records) {
        for(CSVRecord record: records) {
            for(String header: headers) {
                String value = record.get(header);
                Map<String, Integer> headerVsValueCount =
                        columnVsValuesCount.getOrDefault(header, new HashMap<>());
                Integer valueCount = headerVsValueCount.getOrDefault(value, 0);
                headerVsValueCount.put(value, valueCount + 1);
                columnVsValuesCount.put(header, headerVsValueCount);
            }
        }
    }

    public void printAllRecords (List<CSVRecord> csvRecords) {
        for(CSVRecord csvRecord: csvRecords) {
            System.out.println(Arrays.toString(csvRecord.values()));
        }
    }

    public Integer getNumberOfSongsInTheFile() {
        return csvRecords.size();
    }

    public Integer getValuesCountForKey(String header, String key) {
        return columnVsValuesCount
                .getOrDefault(header, new HashMap<>())
                .getOrDefault(key, 0);
    }

    public Map<String, String> getMaxValuesForColumn(){
        Map<String, String> maxColumnVsValues = new HashMap<>();
        for(String header: headers) {
            Integer maxCount = 0;
            String maxColumnKey = "";
            Map<String, Integer> columnValues =
                    columnVsValuesCount.getOrDefault(header, new HashMap<>());
            Set<Map.Entry<String, Integer>> entries = columnValues.entrySet();
            for(Map.Entry<String, Integer> entry: entries) {
                String key = entry.getKey();
                Integer count = entry.getValue();
                if(count > maxCount) {
                    maxCount = count;
                    maxColumnKey = key;
                }
            }
            maxColumnVsValues.put(header, maxColumnKey);
        }
        return maxColumnVsValues;
    }
}
