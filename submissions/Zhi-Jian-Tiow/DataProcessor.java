import java.util.HashMap;
import java.util.List;

public class DataProcessor {
    private static List<List<String>> spotifyData;
    private static List<String> header;

    public DataProcessor(List<List<String>> spotifyData, List<String> headers) {
        DataProcessor.spotifyData = spotifyData;
        DataProcessor.header = headers;
    }

    public int getNumberOfSongs() {
        Integer numOfSongs = 0;
        for (int i = 1; i < DataProcessor.spotifyData.size(); i++) {
            numOfSongs++;
        }
        return numOfSongs;
    }

    public HashMap<String, Integer> countNumberOfKey() {
        HashMap<String, Integer> numberOfKey = new HashMap<String, Integer>();
        int indexOfKey = header.indexOf("key");

        for (int i = 0; i < DataProcessor.spotifyData.size(); i++) {
            String key = DataProcessor.spotifyData.get(i).get(indexOfKey);
            numberOfKey.merge(key, 1, Integer::sum);
        }
        return numberOfKey;
    }
}
