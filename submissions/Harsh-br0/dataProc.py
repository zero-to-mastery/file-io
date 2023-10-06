import csv
import os
import sys
from collections import defaultdict


def err(*msg: str):
    print(*msg, file=sys.stderr)
    exit(1)


def load_csv(path):
    try:
        f = open(path)
        return csv.DictReader(f)
    except IOError as e:
        err("Error Occured while opening file: ", e.strerror)

    except csv.Error as e:
        err("Error Occured while reading CSV file: ", str(e))


class Challenge:
    def __init__(self, data: csv.DictReader) -> None:
        self._data = data
        self._functions = ()

        self._result = ()

        self.__state = {}

    def song_count(self):
        self._functions += (
            lambda x, a: 0 if a is None else a + 1 if x["track_name"] is not None else a,
        )
        self._functions[-1]._finalise = lambda a: a

        return self

    def song_count_by_key(self, key: str = "E"):
        self._functions += (lambda x, a: 0 if a is None else a + 1 if x["key"] == key else a,)
        self._functions[-1]._finalise = lambda a: a

        return self

    def most_common_element_by_column(self, col: str = "bpm"):
        self._functions += (
            lambda x, a: (
                defaultdict(int) if a is None else a.update({x[col]: a[x[col]] + 1}) or a
            ),
        )
        self._functions[-1]._finalise = lambda a: max(a, key=a.get)

        return self

    def result(self):

        for f in self._functions:                                    # Initialise State
            self.__state[id(f)] = f(0, None)

        for ent in self._data:                                       # Process Data
            for f in self._functions:
                self.__state[id(f)] = f(ent, self.__state[id(f)])

        for f in self._functions:                                    # finalise output
            self._result += (f._finalise(self.__state[id(f)]),)

        return self._result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        err("Usage: ", sys.argv[0], " {file path}")

    if not (os.path.isfile(sys.argv[1]) and sys.argv[1].endswith("csv")):
        err("Provide a valid CSV file with .csv extension")

    try:
        data = load_csv(sys.argv[1])
        songn, mcelem, mcelem_by_track, songk, songk_by_D = (
            Challenge(data)
            .song_count()
            .song_count_by_key()                                             # default: E
            .song_count_by_key("D")
            .most_common_element_by_column()                                 # default: BPM
            .most_common_element_by_column("track_name")
            .result()
        )

        print(f"""
        Total Songs found in data: {songn}

        Total Songs by key "E": {songk}

        Total Songs by key "D": {songk_by_D}

        Most Common Element by Col "bpm": {mcelem}

        Most Common Element by Col "track_name": {mcelem_by_track}
        """)
        sys.exit(0)

    except Exception as e:
        err("Error Occured: ", str(e))
