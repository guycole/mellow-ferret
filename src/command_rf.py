#
# Title:command_rf.py
# Description: command
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
import logging


class CommandRf:
    def __init__(self):
        self.logger = logging.getLogger()

    def execute(self, command, bc780):
        """
        change radio frequency
        :param command: RF12345678?
        :param bc780: bc780 state
        :return: OK if success
        """
        if command == "RF":
            return f"RF{bc780.frequency}"

        if command.endswith("?"):
            memory_flag = False
            frequency = command[2 : len(command) - 1]
        else:
            memory_flag = True
            frequency = command[2 : len(command)]

        if bc780.set_frequency(frequency, memory_flag) is True:
            return bc780.ok
        else:
            return bc780.empty


# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
