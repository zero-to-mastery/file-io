import 'dart:collection';
import 'dart:convert';
import 'dart:io';

import 'package:csv/csv.dart';

Future<List<List<dynamic>>> readCsv(String path) async {
  try {
    final input = File(path).openRead();
    return await input
        .transform(utf8.decoder)
        .transform(CsvToListConverter())
        .toList();
  } catch (e) {
    print(e);
    throw e;
  }
}

void main() async {
  var rows = await readCsv('spotify-2023.csv');

  final songs = [];

  for (int i = 1; i < rows.length; i++) {
    final Map<dynamic, dynamic> song = HashMap();

    final row = rows[i];

    for (int j = 0; j < row.length; j++) {
      song[rows[0][j]] = row[j];
    }

    songs.add(song);
  }

  // 1. Write a script to identify the number of songs in the file.
  print('The number of songs in the file: ${songs.length}');

  // 2. Write a script that identify the number of songs in the key of E.
  int numberOfSongsInTheKeyOfE = 0;
  songs.forEach((song) {
    if (song['key'] == 'E') numberOfSongsInTheKeyOfE++;
  });

  print('The number of songs in the key of E: ${numberOfSongsInTheKeyOfE}');

  // 3. Count the occurrences of values in a specified column (e.g., artist names) and determine the most common value.
  final Map<dynamic, Map<dynamic, int>> results = HashMap();
  songs.forEach((song) {
    song.forEach((key, value) {
      if (results[key] == null) {
        results[key] = HashMap();
      }

      results[key]![value] = (results[key]![value] ?? 0) + 1;
    });
  });

  results.forEach((key, value) {
    final valueArray = [];
    value.forEach((key, value) {
      valueArray.add([key, value]);
    });

    valueArray.sort(
      (a, b) {
        return b[1] - a[1];
      },
    );

    final mostCommonValue = valueArray[0];
    print(
        'The most common value for ${key}: ${mostCommonValue[0]}. Occurences: ${mostCommonValue[1]}');
  });
}
