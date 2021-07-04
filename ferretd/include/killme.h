/*
** Title:bc780.h
**
** Description:
**   BC780 operations
**
** Development Environment:
**   Ubuntu 18.04.3 LTS (Bionic Beaver)
**   gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1-18.04)
**
** Author:
**   G.S. Cole (guycole at gmail dot com)
*/
#include <string>

#ifndef BC780_H_
#define BC780_H_

class xBc780 {
    std::string installationId;

    public:
        xBc780(const std::string id) {installationId = id;}

        //std::string get_id() {return installationId;}
};

#endif