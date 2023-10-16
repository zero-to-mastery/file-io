const countTotalSongs = require("./utils/countTotalSongs");
const countSongsInKey = require("./utils/countSongsInKey");
const findMostCommonValue = require("./utils/findMostCommonValue");

// Usage
const filePath = "spotify-2023.csv";
countTotalSongs(filePath);
countSongsInKey(filePath, "E");
findMostCommonValue(filePath, "artist(s)_name");
