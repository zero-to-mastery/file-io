package parser;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;

public class CSVFileParser {
    private CSVParser parser;
    public void parseCsv(File file) throws IOException {
        FileReader reader = new FileReader(file);
        parser = CSVParser.parse(reader, CSVFormat.RFC4180
                .builder()
                .setHeader()
                .setSkipHeaderRecord(true)
                .build());
    }

    public List<CSVRecord> getRecords() {
        return parser.getRecords();
    }

    public List<String> getHeaders() {
        return parser.getHeaderNames();
    }
}
