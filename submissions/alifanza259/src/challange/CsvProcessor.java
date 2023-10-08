package challange;

import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import com.opencsv.bean.CsvBindByName;
import com.opencsv.bean.CsvToBeanBuilder;
import com.opencsv.exceptions.CsvValidationException;

public class CsvProcessor {
	public static int numberOfSongs;
	public static int numberOfKeyOfESongs;
	public static String mostCommonArtistName;
	public static int mostCommonArtistNameOccurence;
	
	@CsvBindByName
	private String track_name;

	@CsvBindByName
	private String key;

	@CsvBindByName(column = "artist(s)_name", required = true)
	private String artist_name;

	public static void main(String[] args) throws IOException, CsvValidationException {
		FileReader filereader = new FileReader("./spotify-2023.csv");
		List<CsvProcessor> beans = new CsvToBeanBuilder<CsvProcessor>(filereader).withType(CsvProcessor.class).build()
				.parse();

		Iterator<CsvProcessor> it = beans.stream().iterator();
		Map<String, Integer> artistNameMap = new HashMap<String, Integer>();

		while (it.hasNext()) {
			CsvProcessor row = it.next();
			numberOfSongs++;
			if (row.key.equals("E")) {
				numberOfKeyOfESongs++;
			}
			artistNameMap.put(row.artist_name, artistNameMap.getOrDefault(row.artist_name, 0) + 1);
		}
		
		for(Entry<String, Integer> entry:artistNameMap.entrySet()) {
			if(entry.getValue()>mostCommonArtistNameOccurence) {
				mostCommonArtistName = entry.getKey();
				mostCommonArtistNameOccurence = entry.getValue();
			}
		}
		
		System.out.println("Number of songs in the file: " + numberOfSongs);
		System.out.println("Number of songs in the key of E: " + numberOfKeyOfESongs);
		System.out.println("Most common value for column artists_name: " + mostCommonArtistName);
	}
}
