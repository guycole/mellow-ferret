#
# Title:test_command_rf.py
# Description: test command rf
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
from bc780 import Bc780
from dispatcher import Dispatcher


def test_command_rf():
    bc780 = Bc780()
    dispatcher = Dispatcher()
    result = dispatcher.execute("RF", bc780)
    assert result == "RF87654321"

    result = dispatcher.execute("RF12345678", bc780)
    assert result == bc780.ok

    result = dispatcher.execute("RF12345678?", bc780)
    assert result == bc780.ok


# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
