/*
** Title:bc780.cc
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
#include "bc780.h"

#include <assert.h>
#include <iostream>

Bc780::Bc780(const std::string id) {
    assert(id.empty() == false);

    std::cout << "bc780 " << id << std::endl;
    
    installation_id = id;

//    runMode = ModeType::kManual;
//    frequency = 88500000;
}