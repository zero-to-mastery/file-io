export interface Song {
  track_name: string;
  'artist(s)_name': string;
  artist_count: string;
  released_year: string;
  released_month: string;
  released_day: string;
  in_spotify_playlists: string;
  in_spotify_charts: string;
  streams: string;
  in_apple_playlists: string;
  in_apple_charts: string;
  in_deezer_playlists: string;
  in_deezer_charts: string;
  in_shazam_charts: string;
  bpm: string;
  key: string;
  mode: string;
  'danceability_%': string;
  'valence_%': string;
  'energy_%': string;
  'acousticness_%': string;
  'instrumentalness_%': string;
  'liveness_%': string;
  'speechiness_%': string;
}
