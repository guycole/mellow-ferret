#
# Title:bc780.py
# Description: bc780 state
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
import logging


class Bc780:
    def __init__(self):
        self.logger = logging.getLogger()

        self.frequency = 87654321

        # string constants
        self.empty = ""
        self.ng = "NG"
        self.ok = "OK"
        self.system_information = "SI BC245XLT,000000228,102"
        self.version_revision = "VR1.00"

    def set_frequency(self, candidate, memory_flag):
        """
        tune radio to new frequency
        :param candidate: frequency as 8 digit integer
        :memory_flag: True store frequency in memory
        :return: True if success else False
        """
        if self.test_legal_frequency(candidate) is True:
            self.logger.info(f"accept new frequency:{candidate}")
            self.frequency = candidate
            return True
        else:
            self.logger.info(f"reject bad frequency:{candidate}")
            return False

    def test_legal_frequency(self, candidate):
        """
        Enforce tune command within legal frequency
        :param candidate: frequency to test
        :return: True if legal
        """
        # todo issue 64
        return True


# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
