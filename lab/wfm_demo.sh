#!/bin/bash
#
# Title:wfm_demo.sh
# Description:demonstrate wideband fm
# Development Environment:Ubuntu 18
# Author:G.S. Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
# example from kmkeen.com, does not work
#rtl_fm -M wbfm -f 94.7M | play -r 32k -t raw -e s -b 16 -c l -V1 -
#
# example from rtl_fm man page, does not work
#rtl_fm -M wbfm -f 94.7M | aplay -r 24k -f S16_LE -t raw -c 1
#
# example from luigifcruz, works well
#rtl_fm -M wfm -f 94.7M -g 50 -s 180k -E deemp | play -r 180k -t raw -e s -b 16 -c 1 -V1 - lowpass 16k
#
# example from linux magazine, works well
rtl_fm -f 94.7M -s 200000 -r 48000 | aplay -r 48000 -f S16_LE
#
