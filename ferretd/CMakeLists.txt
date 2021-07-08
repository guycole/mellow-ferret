#
# mellow ferret daemon
#
cmake_minimum_required(VERSION 3.10.2)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp -o3")
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(PROJ_NAME "ferretd")
project(${PROJ_NAME} VERSION 0.0)
configure_file(ferretd_config.h.in ../include/ferretd_config.h)
set(CMAKE_BUILD_TYPE Debug) # Debug, Release, RelWithDebInfo

include_directories("include")

file(GLOB SOURCES "src/*.cc")

# add_executable(${PROJ_NAME} ${SOURCES})

############
set(Boost_USE_STATIC_LIBS OFF) 
set(Boost_USE_MULTITHREADED ON)  
set(Boost_USE_STATIC_RUNTIME OFF) 
find_package(Boost 1.75.0 COMPONENTS date_time filesystem log system) 

if(Boost_FOUND)
    include_directories(${Boost_INCLUDE_DIRS}) 
    add_executable(${PROJ_NAME} ${SOURCES})
    target_link_libraries(${PROJ_NAME} ${Boost_LIBRARIES})
#    add_executable(progname file1.cxx file2.cxx) 
#    target_link_libraries(progname ${Boost_LIBRARIES})
endif()

############

#include_directories(~/Documents/github/mellow-ferret/ferretdlib/include)
#set(PROJECT_LINK_LIBS libferretd.a)
#link_directories(~/Documents/github/mellow-ferret/ferretdlib/build)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/609281088cfefc76f9d0ce82e1ff6c30cc3591e5.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
#set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

add_executable(ferret_test gtestsrc/run_mode.cc)
target_link_libraries(ferret_test gtest_main)

include(GoogleTest)
gtest_discover_tests(ferret_test)
