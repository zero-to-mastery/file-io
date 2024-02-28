import Control.Monad
import Data.Char (toLower)
import Data.List (maximumBy, nub)
import Data.Map qualified as M
import Data.Ord (comparing)
import System.Environment (getArgs)
import Text.CSV (CSV, parseCSV)

data DataObject = DataObject
  { trackName :: String,
    artistName :: String,
    artistCount :: String,
    releasedYear :: String,
    releasedMonth :: String,
    releasedDay :: String,
    inSpotifyPlaylists :: String,
    inSpotifyCharts :: String,
    streams :: String,
    inApplePlaylists :: String,
    inAppleCharts :: String,
    inDeezerPlaylists :: String,
    inDeezerCharts :: String,
    inShazamCharts :: String,
    bpm :: String,
    key :: String,
    mode :: String,
    danceabilityPercentage :: String,
    valencePercentage :: String,
    energyPercentage :: String,
    acousticnessPercentage :: String,
    instrumentalnessPercentage :: String,
    livenessPercentage :: String,
    speechinessPercentage :: String
  }
  deriving (Show)

newtype Analyzer = Analyzer
  { inputData :: [DataObject]
  }

-- Read CSV File to a list of data objects
readCSVContentSkipFirstLine :: FilePath -> IO [DataObject]
readCSVContentSkipFirstLine file = do
  csvData <- readFile file
  case parseCSV file csvData of
    Left err -> do
      putStrLn $ "Error parsing CSV: " ++ show err
      pure []
    Right rows -> do
      let dataObjects = map createDataObject (tail rows)
      -- Print individual fields for validation or debugging
      -- mapM_ printFields dataObjects
      -- Return the list of DataObjects
      pure dataObjects

-- Right rows -> pure $ map createDataObject (tail rows)

-- Print individual fields of a DataObject
printFields :: DataObject -> IO ()
printFields obj = do
  putStrLn $ "Track Name: " ++ trackName obj
  putStrLn $ "Artist Name: " ++ artistName obj
  -- Print other fields as needed
  putStrLn "-------------------------"

-- Create single data object -> Mapp Data from CSV Row into the DataObject Struct
createDataObject :: [String] -> DataObject
createDataObject dataRow =
  DataObject
    { trackName = dataRow !! 0,
      artistName = dataRow !! 1,
      artistCount = dataRow !! 2,
      releasedYear = dataRow !! 3,
      releasedMonth = dataRow !! 4,
      releasedDay = dataRow !! 5,
      inSpotifyPlaylists = dataRow !! 6,
      inSpotifyCharts = dataRow !! 7,
      streams = dataRow !! 8,
      inApplePlaylists = dataRow !! 9,
      inAppleCharts = dataRow !! 10,
      inDeezerPlaylists = dataRow !! 11,
      inDeezerCharts = dataRow !! 12,
      inShazamCharts = dataRow !! 13,
      bpm = dataRow !! 14,
      key = dataRow !! 15,
      mode = dataRow !! 16,
      danceabilityPercentage = dataRow !! 17,
      valencePercentage = dataRow !! 18,
      energyPercentage = dataRow !! 19,
      acousticnessPercentage = dataRow !! 20,
      instrumentalnessPercentage = dataRow !! 21,
      livenessPercentage = dataRow !! 22,
      speechinessPercentage = dataRow !! 23
    }

-- Create a mapping of the input column string to a lambda expression with 
-- a) the function or record field accessor that can be applied to the obj argument
-- b) the const int 1 (needed for solution 3, represents the counter for objects (starts at 1))
mapColumnName :: String -> Maybe (DataObject -> (String, Int))
mapColumnName columnName =
  case map toLower columnName of
    "track_name" -> Just (\obj -> (trackName obj, 1))
    "artist(s)_name" -> Just (\obj -> (artistName obj, 1))
    "artist_count" -> Just (\obj -> (artistCount obj, 1))
    "released_year" -> Just (\obj -> (releasedYear obj, 1))
    "released_month" -> Just (\obj -> (releasedMonth obj, 1))
    "released_day" -> Just (\obj -> (releasedDay obj, 1))
    "in_spotify_playlists" -> Just (\obj -> (inSpotifyPlaylists obj, 1))
    "in_spotify_charts" -> Just (\obj -> (inSpotifyCharts obj, 1))
    "streams" -> Just (\obj -> (streams obj, 1))
    "in_apple_playlists" -> Just (\obj -> (inApplePlaylists obj, 1))
    "in_apple_charts" -> Just (\obj -> (inAppleCharts obj, 1))
    "in_deezer_playlists" -> Just (\obj -> (inDeezerPlaylists obj, 1))
    "in_deezer_charts" -> Just (\obj -> (inDeezerCharts obj, 1))
    "in_shazam_charts" -> Just (\obj -> (inShazamCharts obj, 1))
    "bpm" -> Just (\obj -> (bpm obj, 1))
    "key" -> Just (\obj -> (key obj, 1))
    "mode" -> Just (\obj -> (mode obj, 1))
    "danceability_%" -> Just (\obj -> (danceabilityPercentage obj, 1))
    "valence_%" -> Just (\obj -> (valencePercentage obj, 1))
    "energy_%" -> Just (\obj -> (energyPercentage obj, 1))
    "acousticness_%" -> Just (\obj -> (acousticnessPercentage obj, 1))
    "instrumentalness_%" -> Just (\obj -> (instrumentalnessPercentage obj, 1))
    "liveness_%" -> Just (\obj -> (livenessPercentage obj, 1))
    "speechiness_%" -> Just (\obj -> (speechinessPercentage obj, 1))
    _ -> Nothing

main :: IO ()
main = do
  args <- getArgs
  if null args
    then
      putStrLn "For [Solution 3], please provide the column name as command line arg."
        >> putStrLn "Possible values: track_name, artist(s)_name, artist_count, released_year, released_month, released_day,"
        >> putStrLn "in_spotify_playlists, in_spotify_charts, streams, in_apple_playlists, in_apple_charts,"
        >> putStrLn "in_deezer_playlists, in_deezer_charts, in_shazam_charts, bpm, key, mode,"
        >> putStrLn "danceability_%, valence_%, energy_%, acousticness_%,"
        >> putStrLn "instrumentalness_%, liveness_%, speechiness_%"
    else do
      let columnName = head args
      let mappedColumn = mapColumnName columnName
      fileData <- readCSVContentSkipFirstLine "data/spotify-clean.csv"
      let analyzer = Analyzer fileData

      -- Solution 1
      let numberOfSongs = getNumberOfSongsInFile analyzer
      putStrLn $ "[Solution 1]: Number of unique songs: " ++ show numberOfSongs

      -- Solution 2
      let numberOfSongsWithKeyE = getNumberOfSongsInFileWithKeyE analyzer
      putStrLn $ "[Solution 2]: Number of unique songs with Key 'E': " ++ show numberOfSongsWithKeyE

      -- Solution 3
      case mappedColumn of
        Just column -> findMostCommonValueInSpecifiedColumn analyzer columnName column
        Nothing -> putStrLn "Invalid column name provided"

-- counts all unique names in the trackName column
getNumberOfSongsInFile :: Analyzer -> Int
getNumberOfSongsInFile analyzer = length $ nub $ map trackName $ inputData analyzer

-- counts all unique values with the exact letter E in the key field
getNumberOfSongsInFileWithKeyE :: Analyzer -> Int
getNumberOfSongsInFileWithKeyE analyzer = length $ filter hasKeyE (inputData analyzer)
  where
    hasKeyE :: DataObject -> Bool
    hasKeyE dataObject = key dataObject == "E"

-- Finds the most common value in a user specified column
-- Inputs: 
-- 1) The user input column name
-- 2) the Lambda expression based on the input. Example: (\obj -> (trackName obj, 1))
findMostCommonValueInSpecifiedColumn :: Analyzer -> String -> (DataObject -> (String, Int)) -> IO ()
findMostCommonValueInSpecifiedColumn analyzer columnInputName column = do
  -- apply the lambda expression to the inputData
  let songCounterMap = map column $ inputData analyzer
  -- foldr is a higher-order function that folds a binary function over a list from right to left. It takes three arguments:
  -- 1) The binary function that combines an element of the list and an accumulator.
  -- 2) The initial accumulator value.
  -- 3) The list to fold.
  -- The lambda function \(key, count) acc -> M.insertWith (+) key count acc takes a tuple (key, count) and an accumulator acc. 
  -- It inserts the tuple into the accumulator map (M.insertWith (+) key count acc). If the key is already present in the map, 
  -- it adds the current count to the existing count using the (+) function.
  -- M.empty is the initial accumulator value, an empty Data.Map.
  -- songCounterMap is the list of tuples that are being folded.
  let groupedMap = foldr (\(key, count) acc -> M.insertWith (+) key count acc) M.empty songCounterMap
  -- select most frequent values based on count - store it in tupel
  let (highScoreKey, highScore) = maximumBy (comparing snd) $ M.toList groupedMap
  -- print result
  putStrLn $ "[Solution 3]: HighScore for column [" ++ columnInputName ++ "]: " ++ highScoreKey ++ ": " ++ show highScore