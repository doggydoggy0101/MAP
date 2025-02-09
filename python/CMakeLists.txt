project(python_wrapper)

pybind11_add_module(map_python map_python/python_wrapper.cpp)

target_link_libraries(map_python PUBLIC MAP::map)

# https://github.com/pybind/pybind11/issues/1818
if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    target_compile_options(map_python PUBLIC -fsized-deallocation)
endif()


SET_TARGET_PROPERTIES(
    map_python
    PROPERTIES 
    PREFIX ""
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/map_python"
)

configure_file(
    map_python/__init__.py
    ${CMAKE_CURRENT_BINARY_DIR}/map_python/__init__.py 
)

configure_file(
    setup.py.in
    ${CMAKE_CURRENT_BINARY_DIR}/setup.py
)

file(
    COPY .
    DESTINATION .
    FILES_MATCHING
    PATTERN *.py
)