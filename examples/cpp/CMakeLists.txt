cmake_minimum_required(VERSION 3.11)
project(map_example)
set(CMAKE_CXX_STANDARD 17)

add_subdirectory(${CMAKE_SOURCE_DIR}/../.. ${CMAKE_BINARY_DIR}/MAP)

add_executable(map_example map_example.cpp)
target_link_libraries(map_example PRIVATE MAP::map)