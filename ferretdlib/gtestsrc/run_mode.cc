/*
** Title:run_mode.cc
**
** Description:
**   test run mode
**
** Development Environment:
**   Ubuntu 18.04.3 LTS (Bionic Beaver)
**   gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1-18.04)
**
** Author:
**   G.S. Cole (guycole at gmail dot com)
*/
#include "gtest/gtest.h"

#include "run_mode.h"

// test suite, test name
TEST(SomeTestSuite, SomeTest) {
    RunMode *obj = new RunMode();
    obj->set_mode(ModeType::kManual);
    ASSERT_EQ(obj->get_mode(), ModeType::kManual);
}