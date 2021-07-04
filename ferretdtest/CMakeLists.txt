#
# mellow ferret daemon library test
#
cmake_minimum_required(VERSION 3.10.2)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(PROJ_NAME "ferretdtest")
project(${PROJ_NAME} LANGUAGES CXX)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/609281088cfefc76f9d0ce82e1ff6c30cc3591e5.zip
)

FetchContent_MakeAvailable(googletest)

enable_testing()

file(GLOB SOURCES "src/*.cpp")
add_executable(hello_test ${SOURCES})
target_link_libraries(hello_test gtest_main)

include(GoogleTest)
gtest_discover_tests(hello_test)