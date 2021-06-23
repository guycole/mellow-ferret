#
# Title:command_cb.py
# Description: command
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
import logging

class CommandCb:
    def __init__(self):
        self.logger = logging.getLogger()

    def execute(self, command, bc780):
        self.logger.info(f"command:{command}")
        return "CB\r"

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***