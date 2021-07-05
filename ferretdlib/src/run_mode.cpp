/*
** Title:run_mode.cpp
**
** Description:
**   Emulate BC780 state
**
** Development Environment:
**   Ubuntu 18.04.3 LTS (Bionic Beaver)
**   gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1-18.04)
**
** Author:
**   G.S. Cole (guycole at gmail dot com)
*/
#include "run_mode.h"

void RunMode::set_mode(ModeType arg) {
    mode = arg;
}
