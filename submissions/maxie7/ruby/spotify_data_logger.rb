require 'csv'

# Read the CSV file with specified encoding
csv_file = '../../../spotify-2023.csv'
songs = CSV.read(csv_file, headers: true, encoding: 'ISO-8859-1')

number_of_songs = songs.length
songs_in_key_of_E = 0

songs.each do |song|
  key = song['key']
  if key == 'E'
    songs_in_key_of_E += 1
  end
end

column_to_count = 'artist(s)_name'
value_count = {}

songs.each do |song|
  value = song[column_to_count]
  if value_count[value]
    value_count[value] += 1
  else
    value_count[value] = 1
  end
end

most_common_value = value_count.max_by { |k, v| v }

puts "Number of songs in the file: #{number_of_songs}"
puts "Number of songs in the key of E: #{songs_in_key_of_E}"
puts "Most common #{column_to_count}: #{most_common_value[0]} (Count: #{most_common_value[1]})"