/*
** Title:
**   driver.cc
**
** Description:
**   start ferretd
**
** Development Environment:
**   Ubuntu 18.04.3 LTS (Bionic Beaver)
**   gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1-18.04)
**
** Author:
**   G.S. Cole (guycole at gmail dot com)
*/
#include<iostream>

#include <boost/log/trivial.hpp>

#include "bc780.h"
#include "ferretd_config.h"

int main(int argc, char *argv[]) {
   std::cout << "ferretd driver " << FERRETD_VERSION_MAJOR << "." << FERRETD_VERSION_MINOR << std::endl;

   BOOST_LOG_TRIVIAL(trace) << "A trace severity message";
   BOOST_LOG_TRIVIAL(debug) << "A debug severity message";
   BOOST_LOG_TRIVIAL(info) << "An informational severity message";
   BOOST_LOG_TRIVIAL(warning) << "A warning severity message";
   BOOST_LOG_TRIVIAL(error) << "An error severity message";
   BOOST_LOG_TRIVIAL(fatal) << "A fatal severity message";

   Bc780 bc780("testaroo");
   std::cout << bc780.get_id() << std::endl;

   return 0;
}
