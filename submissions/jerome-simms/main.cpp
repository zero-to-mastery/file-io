#include <iostream>
#include "SpotifyDataSolver.h"

int main()
{
    SpotifyDataSolver solver{};

    // print out the total number of songs in the csv
    std::cout << "There are " << solver.get_song_count()
        << " somgs in the csv" << std::endl;

    // print out the number of songs in the key E
    std::cout << "There are " << solver.count_occurances("key", "E")
        << " songs in the key E" << std::endl;

    // finding the most common key in the dataset
    std::cout << "The most common key in the data is "
        << solver.get_most_common_in_column("key") << std::endl;

    
    return EXIT_SUCCESS;
}