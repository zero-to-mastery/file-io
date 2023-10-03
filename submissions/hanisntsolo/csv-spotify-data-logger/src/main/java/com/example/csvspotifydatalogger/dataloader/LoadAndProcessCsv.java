package com.example.csvspotifydatalogger.dataloader;

import com.example.csvspotifydatalogger.service.SpotifyService;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.event.EventListener;
import org.springframework.stereotype.Component;


@Component
public class LoadAndProcessCsv {

    @Value("${spring.datasource.url}")
    String url = "";
    @Value("${spring.datasource.username}")
    String userName;
    @Value("${spring.datasource.password}")
    String password;
    @Value("${spring.datasource.driverClassName}")
    String driver;
    @Value("${path.to.csv}")
    String pathToCsv = "E:\\.code\\file-io\\submissions\\hanisntsolo\\csv-spotify-data-logger\\src\\main\\resources\\spotify-2023.csv";

    @Autowired
    SpotifyService spotifyService;

    @EventListener(ApplicationReadyEvent.class)
    public void loadCSVDataToDatabase()
        throws FileNotFoundException, SQLException, IOException, ClassNotFoundException {
        // Create a connection to an in-memory database
        Connection connection = DriverManager.getConnection(url, userName, password);
            PreparedStatement statement = connection.prepareStatement(
                "INSERT INTO spotify_table "
                    + "(id, track_name,artist_name,artist_count,released_year,released_month,released_day,in_spotify_playlists,"
                    + "in_spotify_charts,streams,in_apple_playlists,in_apple_charts,in_deezer_playlists,in_deezer_charts,"
                    + "in_shazam_charts,track_bpm,track_key,track_mode,danceability,valence,energy,acousticness,instrumentalness,liveness,speechiness) "
                + "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");

            // Read the CSV file and load the data into the table
            BufferedReader reader = new BufferedReader(new FileReader(pathToCsv));
            String line;
            long id = 1;
            while ((line = reader.readLine()) != null) {
                List<String> values = new ArrayList<>(Arrays.asList(line.split(",")));
                statement.setLong(1, id++);
                for(int i = 1; i < 25; i++) {
                    statement.setString(i+1, values.get(i-1));
                }
                statement.executeUpdate();
            }
            reader.close();
            // Close the prepared statement and connection
            statement.close();
            connection.close();
            checkData();
            String key = "125";
            mostCommonValueInAColumn("danceability", "SPOTIFY_TABLE");
        System.out.println("Total Number of Songs with a give key :: "+ key + " :: " + countNumberOfSongsWithAGivenKey(key));
        System.out.println("Total Number of Songs :: " + countNumberOfSongs());
    }

    public void checkData() throws SQLException {
        Connection connection = DriverManager.getConnection(url, userName, password);
        Statement statement = connection.createStatement();
        String query = "select * from SPOTIFY_TABLE";
        try {
            ResultSet resultSet = statement.executeQuery(query);
            // Process the results
            while (resultSet.next()) {
                // Retrieve data from each column
                int id = resultSet.getInt("id");
                String trackName = resultSet.getString("track_name");
                String artistName = resultSet.getString("artist_name");
                // Retrieve other columns as needed

                // Print or process the retrieved data
                System.out.print("ID: " + id + " ");
                System.out.print("Track Name: " + trackName+ " ");
                System.out.print("Artist Name: " + artistName+ " ");
                System.out.println();
                // Print or process other columns
            }

            // Close resources
            resultSet.close();
            statement.close();
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public int mostCommonValueInAColumn(String columnName, String tableName) throws SQLException {
        Connection connection = DriverManager.getConnection(url, userName, password);
        Statement statement = connection.createStatement();
        String query = "SELECT "+columnName+", COUNT(*) as occurrence_count\n"
            + "FROM "+tableName+" \n"
            + "GROUP BY "+columnName+"\n"
            + "ORDER BY occurrence_count DESC\n"
            + "LIMIT 1;\n";
        try {
            ResultSet resultSet = statement.executeQuery(query);
            // Process the results
            while (resultSet.next()) {
                // Retrieve data from each column
                String value = resultSet.getString(columnName);
                // Retrieve other columns as needed

                // Print or process the retrieved data
                System.out.println("Most common value in " + columnName + " in " + tableName);
                System.out.print("is" +columnName + " ::  " + value+ " ");
                System.out.println();
                // Print or process other columns
            }

            // Close resources
            resultSet.close();
            statement.close();
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return 0;
    }
    public int countNumberOfSongsWithAGivenKey(String key) {
        return spotifyService.countSongsWithAGivenKey(key);
    }
    public int countNumberOfSongs() {
        return spotifyService.count();
    }
}
