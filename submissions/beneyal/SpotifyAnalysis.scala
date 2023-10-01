//> using dep "com.github.tototoshi::scala-csv:1.3.10"

import com.github.tototoshi.csv.*
import java.io.File

object SpotifyAnalysis {
  val ARTIST_NAME_COLUMN = "artist(s)_name"
  val KEY_COLUMN         = "key"

  def main(args: Array[String]): Unit = {
    val reader                    = CSVReader.open(new File("../../spotify-2023.csv"))
    val lines                     = reader.allWithHeaders()
    val numberOfSongs             = lines.length
    val numberOfSongsInE          = lines.filter(line => line(KEY_COLUMN) == "E").length
    val artistHistogram           = lines.groupBy(line => line(ARTIST_NAME_COLUMN)).view.mapValues(_.length).toMap
    val (mostCommonArtist, count) = artistHistogram.maxBy(_._2)

    println(s"There are $numberOfSongs songs in the dataset, $numberOfSongsInE of which are in the key of E.")
    println(s"The most common artist in the dataset is $mostCommonArtist with $count songs.")
  }
}
