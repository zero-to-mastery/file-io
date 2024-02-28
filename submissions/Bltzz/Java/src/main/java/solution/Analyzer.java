package solution;

import java.io.FileReader;
import java.io.Reader;
import java.lang.reflect.InvocationTargetException;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.stream.Collectors;

import com.opencsv.CSVParser;
import com.opencsv.CSVParserBuilder;
import com.opencsv.CSVReader;
import com.opencsv.CSVReaderBuilder;
import com.opencsv.bean.CsvToBeanBuilder;

import dataObject.DataObject;

public class Analyzer {

	private final static String filePath = "data/spotify-clean.csv";

	private List<DataObject> inputData;

	public Analyzer() {
		this.inputData = readCsvContentSkipFirstLine(filePath);
	}

	public static void main(String[] args) {
		Analyzer analyzer = new Analyzer();

		/**
		 * Solution 1
		 */
		int numberOfSongs = analyzer.getNumberOfSongsInFile();
		System.out.println("Solution 1:");
		System.out.println("Total number of unique songs: " + numberOfSongs);

		/**
		 * Solution 2
		 */
		int numberOfSongsWithKeyE = analyzer.getNumberOfSongsWithKeyE();
		System.out.println("Solution 2:");
		System.out.println("Total number of unique songs with Key 'E': " + numberOfSongsWithKeyE);

		/**
		 * Solution 3
		 */
		if (args.length == 2 && "--column".equals(args[0])) {
			String columnToArgMapping = analyzer.getColumnToArgMapping(args[1]);
			Map<Object, Long> occurrencesMap = analyzer.countOccurrences(columnToArgMapping);

			// Determine the most common value
			String mostCommonValue = analyzer.findMostCommonValue(occurrencesMap);
			Long mostCommonValueCount = analyzer.findMostCommonValueCount(occurrencesMap);
			System.out.println("Solution 3:");
			System.out.println("Most frequent entry in columen [" + args[1] + "] is: " + mostCommonValue + " with "
					+ mostCommonValueCount + " entries.");
		} else {
			System.out.println("For Solution 3, please prove a value like this: ");
			System.out.println("java -jar Analyzer-jar-with-dependencies.jar --column [column]");
		}
	}

	private String getColumnToArgMapping(String columnname) {

		switch (columnname) {
		case "track_name":
			return "trackName";

		case "artist(s)_name":
			return "artistName";

		case "artist_count":
			return "artistCount";

		case "released_year":
			return "releasedYear";

		case "released_month":
			return "releasedMonth";
		case "released_day":
			return "releasedDay";
		case "in_spotify_playlists":
			return "inSpotifyPlaylists";
		case "in_spotify_charts":
			return "inSpotifyCharts";
		case "streams":
			return "streams";
		case "in_apple_playlists":
			return "inApplePlaylists";
		case "in_apple_charts":
			return "inAppleCharts";
		case "in_deezer_playlists":
			return "inDeezerPlaylists";
		case "in_deezer_charts":
			return "inDeezerCharts";
		case "in_shazam_charts":
			return "inShazamCharts";
		case "bpm":
			return "bpm";
		case "key":
			return "key";
		case "mode":
			return "mode";
		case "danceability_%":
			return "danceabilityPercentage";
		case "valence_%":
			return "valencePercentage";
		case "energy_%":
			return "energyPercentage";
		case "acousticness_%":
			return "acousticnessPercentage";
		case "instrumentalness_%":
			return "instrumentalnessPercentage";
		case "liveness_%":
			return "livenessPercentage";
		case "speechiness_%":
			return "speechinessPercentage";
		}
		return columnname;
	}

	private int getNumberOfSongsInFile() {
		Set<String> uniqueSongs = new HashSet<>();
		for (DataObject obj : this.getInputData()) {
			uniqueSongs.add(obj.getTrackName());
		}
		return uniqueSongs.size();
	}

	private int getNumberOfSongsWithKeyE() {
		Set<String> uniqueSongs = new HashSet<>();
		for (DataObject obj : this.getInputData()) {
			if ("E".equals(obj.getKey()))
				uniqueSongs.add(obj.getTrackName());
		}
		return uniqueSongs.size();
	}

	private Map<Object, Long> countOccurrences(String columnName) {
		// Use Java streams to group by the specified column and count occurrences
		return this.getInputData().stream().collect(Collectors.groupingBy(trackBean -> {
			try {
				return getColumnValue(trackBean, columnName);
			} catch (InvocationTargetException | NoSuchMethodException | SecurityException e) {
				System.err.println(e);
			}
			return null;
		}, Collectors.counting()));
	}

	private String findMostCommonValue(Map<Object, Long> occurrencesMap) {
		// Find the entry with the maximum count
		Entry<Object, Long> maxEntry = occurrencesMap.entrySet().stream().max(Map.Entry.comparingByValue())
				.orElse(null);
		return (maxEntry != null) ? (String) maxEntry.getKey() : null;
	}

	private Long findMostCommonValueCount(Map<Object, Long> occurrencesMap) {
		// Find the entry with the maximum count
		Entry<Object, Long> maxEntry = occurrencesMap.entrySet().stream().max(Map.Entry.comparingByValue())
				.orElse(null);

		return (maxEntry != null) ? maxEntry.getValue() : null;
	}

	private String getColumnValue(DataObject trackBean, String columnName)
			throws InvocationTargetException, NoSuchMethodException, SecurityException {
		// Use reflection to get the value of the specified column
		try {
			return (String) trackBean.getClass()
					.getMethod("get" + columnName.substring(0, 1).toUpperCase() + columnName.substring(1))
					.invoke(trackBean);
		} catch (IllegalAccessException e) {
			e.printStackTrace();
			return null;
		}
	}

	public List<DataObject> getInputData() {
		return this.inputData;
	}

	private List<DataObject> readCsvContentSkipFirstLine(String path) {

		try (Reader reader = new FileReader(path)) {
			CSVParser csvParser = new CSVParserBuilder().withSeparator(';').withQuoteChar('\"').build();

			CSVReader csvReader = new CSVReaderBuilder(reader).withCSVParser(csvParser).build();
			String[] header = csvReader.readNext();

			if (header != null) {
				// Create CsvToBean with header and type
				List<DataObject> beans = new CsvToBeanBuilder<DataObject>(csvReader).withType(DataObject.class)
						.withIgnoreLeadingWhiteSpace(true).build().parse();
				return beans;
			} else {
				System.out.println("CSV file is empty or does not have a header.");
			}

		} catch (Exception e) {
			System.err.println("Exception while reading csv [" + path + "] " + e);
		}
		return null;

	}
}
