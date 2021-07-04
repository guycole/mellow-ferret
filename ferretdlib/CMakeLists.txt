#
# mellow ferret daemon library
#
cmake_minimum_required(VERSION 3.10.2)

set(PROJ_NAME "ferretdlib")
project(${PROJ_NAME})

# Debug, Release, RelWithDebInfo
set(CMAKE_BUILD_TYPE Debug)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

include_directories("include")

file(GLOB SOURCES "src/*.cpp")

# SHARED, STATIC or MODULE
add_library(ferretd STATIC ${SOURCES})

#install(TARGETS ferretd DESTINATION /usr/local/lib)