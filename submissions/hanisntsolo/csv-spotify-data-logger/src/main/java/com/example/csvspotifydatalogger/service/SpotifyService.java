package com.example.csvspotifydatalogger.service;

import com.example.csvspotifydatalogger.model.SpotifyTable;
import com.example.csvspotifydatalogger.repository.SpotifyRepository;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class SpotifyService {

    @Autowired
    private SpotifyRepository spotifyRepository;

    public List<SpotifyTable> getAllEntries() {
        return spotifyRepository.findAll();
    }
    public int count() {
        return (int) spotifyRepository.count();
    }
    public int countSongsWithAGivenKey(String key) {
        return (int) spotifyRepository.countSongsByKey(key);
    }
}
