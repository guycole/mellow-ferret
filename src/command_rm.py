#
# Title:command_rm.py
# Description: modulation
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
import logging

from bc780 import Bc780

class CommandRm:
    def __init__(self):
        self.logger = logging.getLogger()

    def execute(self, command:str, bc780:Bc780):
        self.logger.info(f"command:{command}")
        return "RM\r"

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***