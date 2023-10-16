package com.example.csvspotifydatalogger.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Table;

@Entity
@Table(name ="spotify_table")
public final class SpotifyTable {

   @jakarta.persistence.Id
   @GeneratedValue(strategy = GenerationType.AUTO)
   private Long id;
   @Column(name = "track_key")
   String key;
   @Column(name = "track_name")
   String track_name;
   @Column(name = "artist_name")
   String artist_name;
   @Column(name = "artist_count")
   String artist_count;
   @Column(name = "released_year")
   String released_year;
   @Column(name = "released_month")
   String released_month;
   @Column(name = "released_day")
   String released_day;
   @Column(name = "in_spotify_playlists")
   String in_spotify_playlists;
   @Column(name = "in_spotify_charts")
   String in_spotify_charts;
   @Column(name = "streams")
   String streams;
   @Column(name = "in_apple_playlists")
   String in_apple_playlists;
   @Column(name = "in_apple_charts")
   String in_apple_charts;
   @Column(name = "in_deezer_playlists")
   String in_deezer_playlists;
   @Column(name = "in_deezer_charts")
   String in_deezer_charts;
   @Column(name = "in_shazam_charts")
   String in_shazam_charts;
   @Column(name = "track_bpm")
   String bpm;
   @Column(name = "track_mode")
   String mode;
   @Column(name = "danceability")
   String danceability;
   @Column(name = "valence")
   String valence;
   @Column(name = "energy")
   String energy;
   @Column(name = "acousticness")
   String acousticness;
   @Column(name = "instrumentalness")
   String instrumentalness;
   @Column(name = "liveness")
   String liveness;
   @Column(name = "speechiness")
   String speechiness;

   public void setId(Long id) {
      this.id = id;
   }

   public Long getId() {
      return id;
   }
}
