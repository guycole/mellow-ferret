#
# Title:dispatcher.py
# Description: command dispatch
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
import logging

class Dispatcher:
    def __init__(self):
        self.logger = logging.getLogger()

    def execute(self, command:str):
        print(f"execute:{str}")

        if str == 'SI':
            pass
        else:
            self.logger.error(f"unknown command:{command}")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***