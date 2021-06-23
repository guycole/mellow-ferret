#
# Title:command_rf.py
# Description: tune receiver but not store frequency
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
import logging

from bc780 import Bc780

class CommandRf:
    def __init__(self):
        self.logger = logging.getLogger()

    def execute(self, command:str, bc780:Bc780):
        self.logger.info(f"command:{command}")
        
        # TODO parse frequency

        bc780.tune_receiver(0)
        return bc780.ok

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***