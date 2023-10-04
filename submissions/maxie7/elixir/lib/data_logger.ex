defmodule DataLogger do
  @moduledoc """
  The functions in the module `DataLogger` resolve the task of hacktoberfest-2023.
  """

  def output_the_results do
    {artist_name, songs_count} = get_most_common_artist()

    IO.inspect("Total Songs >> #{get_rows()}")
    IO.puts("Total songs in key E >> #{get_songs_in_key_E()}")
    IO.puts("The most common artist is >> #{artist_name} << with the most songs >> #{songs_count}")
  end

  def get_rows do
    File.stream!("../../../spotify-2023.csv")
    |> Stream.drop(1) # Skip the header row
    |> Enum.count()
  end

  def get_songs_in_key_E do
    File.stream!("../../../spotify-2023.csv")
    |> Stream.drop(1)
    |> Stream.filter(&is_key_E?(&1))
    |> Enum.count()
  end

  def get_most_common_artist do
    File.stream!("../../../spotify-2023.csv")
    |> Stream.drop(1)
    |> Stream.map(&String.split(&1, ",", trim: true))
    |> Stream.map(fn [_, artist_names | _] -> artist_names end)
    |> Enum.reduce(%{}, fn artist_name, acc -> Map.update(acc, artist_name, 1, &(&1 + 1)) end)
    |> Enum.max_by(fn {_artist_name, count} -> count end)
  end

  defp is_key_E?(line) do
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, key | _] = String.split(line, ",", trim: true)
    key == "E"
  end
end
