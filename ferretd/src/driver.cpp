/*
** Title:
**   driver.cpp
**
** Description:
**
** Development Environment:
**   Ubuntu 18.04.3 LTS (Bionic Beaver)
**   gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1-18.04)
**
** Author:
**   G.S. Cole (guycole at gmail dot com)
*/
#include<iostream>

#include "bc780.h"

int main(int argc, char *argv[]) {
   std::cout << "ferret driver" << std::endl;

   Bc780 bc780("testaroo");
   std::cout << bc780.get_id() << std::endl;

   return 0;
}