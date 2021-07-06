#
# mellow ferret daemon library
#
cmake_minimum_required(VERSION 3.10.2)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp -o3")
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(PROJ_NAME "ferretd")
project(${PROJ_NAME})
set(CMAKE_BUILD_TYPE Debug) # Debug, Release, RelWithDebInfo

include_directories("include")

file(GLOB SOURCES "src/*.cc")

add_library(${PROJ_NAME} STATIC ${SOURCES}) # SHARED, STATIC or MODULE

#install(TARGETS ferretd DESTINATION /usr/local/lib)

add_subdirectory(googletest)
target_compile_definitions(gtest PUBLIC GTEST_LANG_CXX11)

add_executable(gtestbin gtestsrc)
target_sources(gtestbin PRIVATE gtestsrc/run_mode.cc)

set_target_properties(gtestbin PROPERTIES COMPILE_FLAGS "${cxx_strict}")
target_link_libraries(gtestbin gtest gtest_main)
