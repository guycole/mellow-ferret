cmake_minimum_required(VERSION 3.10.2)

# set the project name
project(ferret)

#include_directories(include)
file(GLOB SOURCES "ferretd/src/*.cpp")

# add the executable
add_executable(ferretd ${SOURCES}) 