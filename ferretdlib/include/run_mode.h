/*
** Title:run_mode.h
**
** Description:
**   Operationanl run mode parent
**
** Development Environment:
**   Ubuntu 18.04.3 LTS (Bionic Beaver)
**   gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1-18.04)
**
** Author:
**   G.S. Cole (guycole at gmail dot com)
*/
#ifndef RUN_MODE_H_
#define RUN_MODE_H_

enum class ModeType {kUnknown, kManual, kScan, kSearch};

class RunMode {
    ModeType mode = ModeType::kUnknown;

    int current_frequency;
 
    public:
        RunMode() {}
        ~RunMode() {}

        void set_mode(ModeType arg);
};

#endif