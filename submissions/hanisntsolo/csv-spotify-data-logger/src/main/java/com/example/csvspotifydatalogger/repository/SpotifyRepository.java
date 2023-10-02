package com.example.csvspotifydatalogger.repository;

import com.example.csvspotifydatalogger.model.SpotifyTable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

public interface SpotifyRepository extends JpaRepository<SpotifyTable, Long> {

    @Query("SELECT COUNT(s) FROM SpotifyTable s WHERE s.key = :key")
    long countSongsByKey(@Param("key") String key);
}
