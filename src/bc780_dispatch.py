#
# Title:bc780_dispatch.py
# Description: command dispatch
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
import logging

from bc780 import Bc780

from command_cb import CommandCb
from command_rf import CommandRf
from command_vr import CommandVr

class Bc780Dispatch:
    def __init__(self):
        self.logger = logging.getLogger()

    def execute(self, command:str, bc780:Bc780):
        self.logger.info(f"command:{command}")

        if command.startswith('AC'):
            # AC = Memory Clear
            pass
        elif command.startswith('AF'):
            # AF = EDACS ID mode
            pass
        elif command.startswith('AL'):
            # AL = Auto Light Function
            pass
        elif command.startswith('AR'):
            # AR = Recording Function
            pass
        elif command.startswith('AT'):
            # AT = Attenuator Function
            pass
        elif command.startswith('BA'):
            # BA = Channel Beep Alert
            pass
        elif command.startswith('BP'):
            # BP = Beep Alert Toggle
            pass
        elif command.startswith('BT'):
            # BT = Motorola Status Bit
            pass
        elif command.startswith('CB'):
            # CB = Choose Active Banks
            command_cb = CommandCb()
            return command_cb.execute(command, bc780)
        elif command.startswith('CC'):
            # CC = Test CTCSS Decode
            pass
        elif command.startswith('CD'):
            # CD = Test CTCSS Detection
            pass
        elif command.startswith('CS'):
            # CS = CTCSS Tone Detect
            pass
        elif command.startswith('CT'):
            # CT = CTCSS Function
            pass
        elif command.startswith('DL'):
            # DL = Delay Function
            pass
        elif command.startswith('DS'):
            # DS = Data Skip Function
            pass
        elif command.startswith('EL'):
            # EL = Edit Lock Function
            pass
        elif command.startswith('FB'):
            # FB = Fleet Map Assignment
            pass
        elif command.startswith('FI'):
            # FI = Frequency Find Function
            pass
        elif command.startswith('FP'):
            # FP = FIPS Weather Code
            pass
        elif command.startswith('IC'):
            # IC = Talk Group ID
            pass
        elif command.startswith('ID'):
            # ID = Trunk Monitor Notification
            pass
        elif command.startswith('IL'):
            # IL = Lockout Memory
            pass
        elif command.startswith('IR'):
            # IR = ICALL Operations
            pass
        elif command.startswith('IS'):
            # IS = Scan List ID
            pass
        elif command.startswith('KEY'):
            # KEY
            pass
        elif command.startswith('LCD'):
            # LCD
            pass
        elif command.startswith('LL'):
            # LL = Lower Search Limit
            pass
        elif command.startswith('LM'):
            # LM = Screen Mask
            pass
        elif command.startswith('LO'):
            # LO = Lockout Channel
            pass
        elif command.startswith('LT'):
            # LT = LCD Illumination
            pass
        elif command.startswith('LU'):
            # LU = Upper Search Limit
            pass
        elif command.startswith('MA'):
            # MA = Memory Access
            pass
        elif command.startswith('MD'):
            # MD = Mode
            pass
        elif command.startswith('MU'):
            # MU = Mute
            pass
        elif command.startswith('PC'):
            # PC = Priority Channel
            pass
        elif command.startswith('PI'):
            # PI = Priority Bank ID
            pass
        elif command.startswith('PM'):
            # PM = Print Memory Data
            pass
        elif command.startswith('PR'):
            # PR = Priority Scan Function
            pass
        elif command.startswith('QU'):
            # QU = Squelch Notification
            pass
        elif command.startswith('RF'):
            # RF = Receiver Frequency
            command_rf = CommandRf()
            return command_rf.execute(command, bc780)
        elif command.startswith('RG'):
            # RG = Radio ID Group
            pass
        elif command.startswith('RI'):
            # RI = Priority Notification
            pass
        elif command.startswith('RM'):
            # RM = Receiver Modulation
            pass
        elif command.startswith('SB'):
            # SB = Select Banks
            pass
        elif command.startswith('SG'):
            # SG = Signal Strength
            pass
        elif command.startswith('SI'):
            # SI = System Information
            pass
        elif command.startswith('SQ'):
            # SQ = Squelch Query
            pass
        elif command.startswith('SS'):
            # SS = Search Skip
            pass
        elif command.startswith('ST'):
            # ST = Step Size
            pass
        elif command.startswith('TA'):
            # TA = Tag Alphanumeric
            pass
        elif command.startswith('TB'):
            # TB = Trunked Bank Info
            pass
        elif command.startswith('TC'):
            # TC = Control Only
            pass
        elif command.startswith('TD'):
            # TD = Trunked Data Bit
            pass
        elif command.startswith('TG'):
            # TG = Talk Group ID
            pass
        elif command.startswith('TR'):
            # TR = Trunk System Type
            pass
        elif command.startswith('VR'):
            # VR = Version Revision
            command_vr = CommandVr()
            return command_vr.execute(command, bc780)
        elif command.startswith('WA'):
            # WA = Weather Alert
            pass
        elif command.startswith('WI'):
            # WI = Window Indication
            pass
        else:
            self.logger.error(f"unknown command:{command}")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***