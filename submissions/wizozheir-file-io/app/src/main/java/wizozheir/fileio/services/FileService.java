package wizozheir.fileio.services;

import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;
import wizozheir.fileio.Song;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.List;

public class FileService {
    private InputStream getInputStreamFromResources(String filename) {
        return getClass().getClassLoader().getResourceAsStream(filename);
    }

    private void printInputStreamLines(InputStream inputStream) throws IOException {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        }
    }


    public List<Song> getSongsFromCSV(String filename) throws IOException {
        try (Reader reader = new InputStreamReader(getInputStreamFromResources(filename))) {
            CsvToBean<Song> csvToBean = new CsvToBeanBuilder<Song>(reader)
                    .withType(Song.class)
                    .build();
            return csvToBean.parse();
        }
    }
}
