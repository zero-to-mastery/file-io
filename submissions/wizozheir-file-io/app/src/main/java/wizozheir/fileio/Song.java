package wizozheir.fileio;

import com.opencsv.bean.CsvBindByName;
import com.opencsv.bean.CsvNumber;
import lombok.Data;

@Data
public class Song {
    @CsvBindByName(column = "track_name")
    private String trackName;

    @CsvBindByName(column = "artist(s)_name")
    private String artistName;

    @CsvBindByName(column = "released_year")
    @CsvNumber("#")
    private int releasedYear;

    @CsvBindByName(column = "released_month")
    @CsvNumber("#")
    private int releasedMonth;

    @CsvBindByName(column = "streams")
    private String streams;

    @CsvBindByName(column = "bpm")
    @CsvNumber("#")
    private int bpm;

    @CsvBindByName(column = "key")
    private String key;
}
