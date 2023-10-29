#pragma once

#include <string>
#include "rapidcsv.h"

class SpotifyDataSolver
{
public:
    SpotifyDataSolver() = default;
    size_t get_song_count();
    size_t count_occurances(const std::string& column_name, const std::string& search_key);
    std::string get_most_common_in_column(const std::string& column_name);

private:
    rapidcsv::Document doc{"spotify-2023.csv"};
};