#include <vector>
#include <string>
#include <unordered_map>
#include "SpotifyDataSolver.h"

size_t SpotifyDataSolver::get_song_count()
{
    return doc.GetRowCount();
}

size_t SpotifyDataSolver::count_occurances(const std::string& column_name, const std::string& search_key)
{
    size_t occurance_count{};

    std::vector<std::string> results{doc.GetColumn<std::string>(column_name)};

    for (const auto& result : results)
    {
        if (result == search_key)
        {
            ++occurance_count;
        }
    }

    return occurance_count;
}

std::string SpotifyDataSolver::get_most_common_in_column(const std::string& column_name)
{
    std::unordered_map<std::string, size_t> kv_map;

    // loop over values in columns
    // if not in map, add to map and set count to 1
    // else increment the value by 1

    std::vector<std::string> results{doc.GetColumn<std::string>(column_name)};
    for (const std::string& result : results)
    {
        size_t val = kv_map[result];
        if (val == 0)
        {
            kv_map[result] = 1;
        }
        else
        {
            ++kv_map[result];
        }
    }

    // loop over kv_map and get the key and value of the largest count / occurances
    std::string name{};
    size_t max_count{};
    for (const std::pair<std::string, size_t>& pair : kv_map)
    {
        if (!max_count)
        {
            name = pair.first;
            max_count = pair.second;
        }

        if (pair.second > max_count)
        {
            name = pair.first;
            max_count = pair.second;
        }
    }

    return name;
}
