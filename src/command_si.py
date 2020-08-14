#
# Title:command_si.py
# Description: return system information
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
import logging

class CommandSi:
    def __init__(self):
        self.logger = logging.getLogger()

    def execute(self, command, bc780):
        return bc780.system_information

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***