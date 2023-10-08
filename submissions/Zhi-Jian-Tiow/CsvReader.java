import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CsvReader {
    private FileReader csvFilePath;
    private List<List<String>> csvData = new ArrayList<>();
    private List<String> header;

    public CsvReader(String csvFilePath) throws FileNotFoundException {
        this.csvFilePath = new FileReader(csvFilePath);
    }

    public void readCSV() throws IOException {
        BufferedReader reader = new BufferedReader(this.csvFilePath);
        String row;
        this.header = List.of(reader.readLine().split(","));
        while ((row = reader.readLine()) != null) {
            String[] rowData = row.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)");
            this.csvData.add(Arrays.asList(rowData));
        }
    }

    public List<List<String>> getCsvData() {
        return this.csvData;
    }

    public List<String> getHeaders() {
        return this.header;
    }
}
