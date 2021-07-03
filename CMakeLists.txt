#
# project comment
#
cmake_minimum_required(VERSION 3.10.2)

project(ferret)

include_directories("ferretd/include")

file(GLOB SOURCES "ferretd/src/*.cpp")

add_executable(ferretd ${SOURCES}) 