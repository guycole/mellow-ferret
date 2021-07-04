#
# mellow ferret daemon
#
cmake_minimum_required(VERSION 3.10.2)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(PROJ_NAME "ferretd")
project(${PROJ_NAME})

# Debug, Release, RelWithDebInfo
set(CMAKE_BUILD_TYPE Debug)

set(PROJECT_LINK_LIBS libferretd.a)
link_directories(~/Documents/github/mellow-ferret/ferretdlib/build)

include_directories("include")
include_directories(~/Documents/github/mellow-ferret/ferretdlib/include)

file(GLOB SOURCES "src/*.cpp")

add_executable(${PROJ_NAME} ${SOURCES})
target_link_libraries(${PROJ_NAME} ${PROJECT_LINK_LIBS})
