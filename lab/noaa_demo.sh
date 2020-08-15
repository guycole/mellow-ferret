#!/bin/bash
#
# Title:noaa_demo.sh
# Description:demonstrate NOAA weather radio
# Development Environment:Ubuntu 18
# Author:G.S. Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
# example from reddit, does not work
rtl_fm -f 162.55M -s 12000 -g 36 -l 150 - | play -t raw -r 12k -e signed-integer -b 16 -c 1 -V1 -
#
