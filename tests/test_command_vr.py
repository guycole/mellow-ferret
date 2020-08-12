#
# Title:test_command_vr.py
# Description: test command vr
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
from bc780 import Bc780
from dispatcher import Dispatcher


def test_command_vr():
    bc780 = Bc780()
    dispatcher = Dispatcher()
    result = dispatcher.execute("VR", bc780)
    assert result == bc780.version_revision


# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
