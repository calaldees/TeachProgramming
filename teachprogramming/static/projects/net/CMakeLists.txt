cmake_minimum_required(VERSION 3.2)
project(demosocket)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp)
add_executable(demosocket ${SOURCE_FILES})

if(WIN32)
  target_link_libraries(demosocket wsock32 ws2_32)
endif()
