#
# Title:command_vr.py
# Description: return version revision
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
import logging

from bc780 import Bc780

class CommandVr:
    def __init__(self):
        self.logger = logging.getLogger()

    def execute(self, command:str, bc780:Bc780):
        return bc780.version_revision

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***