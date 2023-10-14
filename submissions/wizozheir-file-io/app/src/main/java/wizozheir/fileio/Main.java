package wizozheir.fileio;

import wizozheir.fileio.services.FileService;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Main {
    private static final String FILENAME = "spotify-2023.csv";
    private static final String DEFAULT_KEY = "E";

    private static long countSongsWithKey(List<Song> songs, String key) {
        return songs.stream().filter(song -> key.equals(song.getKey())).count();
    }

    private static Map.Entry<String, Long> mostCommonArtist(List<Song> songs) {
        Map<String, Long> artistFrequency = songs.stream()
                .collect(Collectors.groupingBy(Song::getArtistName, Collectors.counting()));

        return artistFrequency.entrySet().stream()
                .max(Map.Entry.comparingByValue())
                .orElse(null);
    }

    public static void main(String[] args) {
        FileService fileService = new FileService();

        try {
            List<Song> songs = fileService.getSongsFromCSV(FILENAME);
            System.out.printf("Total number of songs: %s.%n", songs.size());

            long count = countSongsWithKey(songs, DEFAULT_KEY);
            System.out.printf("Number of songs in the key of %s: %s.%n", DEFAULT_KEY, count);

            Map.Entry<String, Long> mostCommonArtist = mostCommonArtist(songs);
            if (mostCommonArtist != null) {
                System.out.printf("The most common artist is '%s' with %d songs.%n", mostCommonArtist.getKey(), mostCommonArtist.getValue());
            }

        } catch (Exception e) {
            System.out.println("Smth is wrong with file.");
        }


//        System.out.println(String.format("Number of songs in the key of %s: %s" ,
//                DEFAULT_SPECIAL_KEY, processor.countSongsWithSpecialKey(records, DEFAULT_SPECIAL_KEY)));
//
//        Map.Entry<String, Long> mostCommonArtist = processor.mostCommonValueInColumn(records, "Artist");
//        if (mostCommonArtist != null) {
//            System.out.printf("The most common artist is '%s' with %d songs.\n", mostCommonArtist.getKey(), mostCommonArtist.getValue());
//        }
    }
}
