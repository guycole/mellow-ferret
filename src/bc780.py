#
# Title:bc780.py
# Description: bc780 state
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
import logging

class Bc780:
    def __init__(self, installation_id:str):
        self.logger = logging.getLogger()

        self.frequency = 0
        self.installation_id = installation_id
        self.ok = "OK\r"
        self.rf_attenuator = 0
        self.system_information = "SI BC245XLT,000000228,102\r"
        self.version_revision = "VR1.00\r"

    def rf_attenuator(self, arg:int):
        self.logger.info(f"rf_attenuator:{arg}")

    def tune_receiver(self, frequency:int):
        self.logger.info(f"tune_receiver:{frequency}")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***