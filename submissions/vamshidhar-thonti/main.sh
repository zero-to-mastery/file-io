#! /bin/bash

###############################
#  Author: Vamshidhar Thonti  #
#                             #
# Execute cmd: bash ./main.sh #
###############################

TOTAL_TRACKS=$(cat spotify-2023.csv | cut -d ',' -f1 | sed 1,1d | wc -l)
echo "Total number of tracks are ${TOTAL_TRACKS}."
