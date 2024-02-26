require 'csv'

class DataObject
    attr_accessor :track_name, :artist_name, :artist_count, :released_year, :released_month, :released_day,
                  :in_spotify_playlists, :in_spotify_charts, :streams, :in_apple_playlists, :in_apple_charts,
                  :in_deezer_playlists, :in_deezer_charts, :in_shazam_charts, :bpm, :key, :mode,
                  :danceability_percentage, :valence_percentage, :energy_percentage, :acousticness_percentage,
                  :instrumentalness_percentage, :liveness_percentage, :speechiness_percentage

    def initialize(data)
      @track_name = data['track_name']
      @artist_name = data['artist(s)_name']
      @artist_count = data['artist_count']
      @released_year = data['released_year']
      @released_month = data['released_month']
      @released_day = data['released_day']
      @in_spotify_playlists = data['in_spotify_playlists']
      @in_spotify_charts = data['in_spotify_charts']
      @streams = data['streams']
      @in_apple_playlists = data['in_apple_playlists']
      @in_apple_charts = data['in_apple_charts']
      @in_deezer_playlists = data['in_deezer_playlists']
      @in_deezer_charts = data['in_deezer_charts']
      @in_shazam_charts = data['in_shazam_charts']
      @bpm = data['bpm']
      @key = data['key']
      @mode = data['mode']
      @danceability_percentage = data['danceability_%']
      @valence_percentage = data['valence_%']
      @energy_percentage = data['energy_%']
      @acousticness_percentage = data['acousticness_%']
      @instrumentalness_percentage = data['instrumentalness_%']
      @liveness_percentage = data['liveness_%']
      @speechiness_percentage = data['speechiness_%']
    end

    # Mapping between the column names and the actual object variables
    def self.map_column_name(column_name)
      case column_name.downcase
      when "track_name"
        :track_name
      when "artist(s)_name"
        :artist_name
      when "artist_count"
        :artist_count
      when "released_year"
        :released_year
      when "released_month"
        :released_month
      when "released_day"
        :released_day
      when "in_spotify_playlists"
        :in_spotify_playlists
      when "in_spotify_charts"
        :in_spotify_charts
      when "streams"
        :streams
      when "in_apple_playlists"
        :in_apple_playlists
      when "in_apple_charts"
        :in_apple_charts
      when "in_deezer_playlists"
        :in_deezer_playlists
      when "in_deezer_charts"
        :in_deezer_charts
      when "in_shazam_charts"
        :in_shazam_charts
      when "bpm"
        :bpm
      when "key"
        :key
      when "mode"
        :mode
      when "danceability_%"
        :danceability_percentage
      when "valence_%"
        :valence_percentage
      when "energy_%"
        :energy_percentage
      when "acousticness_%"
        :acousticness_percentage
      when "instrumentalness_%"
        :instrumentalness_percentage
      when "liveness_%"
        :liveness_percentage
      when "speechiness_%"
        :speechiness_percentage
      else
        nil # TBD: Handle unknown column names as needed
      end
    end
  end


  class Analyzer
    attr_accessor :input_data

    def initialize(file_path)
      @input_data = read_csv_content_skip_first_line(file_path)
    end

    def get_number_of_songs_in_file
      unique_songs = Set.new
      @input_data.each do |obj|
        unique_songs.add(obj.track_name)
      end
      unique_songs.size
    end

    def get_number_of_songs_in_file_with_key_E
      unique_songs = Set.new
      @input_data.each do |obj|
        if obj.key == 'E'
          unique_songs.add(obj.track_name)
        end
      end
      unique_songs.size
    end

    def find_most_common_value(column_index)
      song_counter_map = Hash.new(0)
      @input_data.each do |obj|
        value = obj.send(column_index)
        song_counter_map[value] += 1
      end

      high_score = 0
      high_score_key = nil

      song_counter_map.each do |key, count|
        if count > high_score
          high_score = count
          high_score_key = key
        end
      end
      puts "HighScore for column #{column_index}: [#{high_score_key}]: #{high_score}"
    end

    # We can do the same as in find_most_common_value, but a bit faster:
    #
    # 1. Step: group the elements of @input_data based on the result of calling obj.send(column_index) for each object.
    # The result is a hash where keys are the unique values of obj.send(column_index)
    # and values are arrays of objects that share the same value.
    # 2. Step: apply transform_values to the hash obtained from group_by.
    # It transforms each value in the hash (which is an array of objects)
    # by applying the count method using the shorthand &:count.
    # This results in a new hash where the keys are the same as before,
    # but the values are the counts of objects in each group.
    # 3. Step: find the pair with the highest count and print these values.
    #
    def find_most_common_value_quick(column_index)
      song_counter_map = @input_data.group_by { |obj| obj.send(column_index) }
                                     .transform_values(&:count)

      high_score_key, high_score = song_counter_map.max_by { |_, count| count }

      puts "HighScore for column #{column_index}: [#{high_score_key}]: #{high_score}"
    end

    private

    def read_csv_content_skip_first_line(file_path)
      csv_data = []
      # Windows encoding, dont care about broken data
      CSV.foreach(file_path, headers: true, encoding: 'ISO-8859-1', invalid: :replace) do |row|
        csv_data << DataObject.new(row)
      end
      csv_data
    end
  end

  # Init
  if ARGV.empty?
    puts "For [Solution 3], please provide the column name as command line arg."
    puts "pussible values: track_name, artist(s)_name, artist_count, released_year, released_month, released_day,
    in_spotify_playlists, in_spotify_charts, streams, in_apple_playlists, in_apple_charts,
    in_deezer_playlists, in_deezer_charts, in_shazam_charts, bpm, key, mode,
    danceability_%, valence_%, energy_%, acousticness_%,
    instrumentalness_%, liveness_%, speechiness_%"
  end

  column_index = ARGV[0]
  mapped_column = DataObject.map_column_name(column_index)

  file_path = 'data/spotify-clean.csv'
  analyzer = Analyzer.new(file_path)

  # Solution 1
  number_of_songs = analyzer.get_number_of_songs_in_file
  puts "Number of unique songs: #{number_of_songs}"

  # Solution 2
  number_of_songs_with_key_e = analyzer.get_number_of_songs_in_file_with_key_E
  puts "Number of unique songs with Key 'E': #{number_of_songs_with_key_e}"

  # Solution 3
  # analyzer.find_most_common_value(mapped_column)
  analyzer.find_most_common_value_quick(mapped_column)
