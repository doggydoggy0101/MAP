include(GNUInstallDirs)

file(GLOB SRC_FILES *.cpp)
file(GLOB HEADER_FILES *.h)

add_library(map SHARED ${SRC_FILES})

target_include_directories(map PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}> 
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

target_link_libraries(map Eigen3::Eigen)
add_library(MAP::map ALIAS map)

install(FILES ${HEADER_FILES} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

install(TARGETS map
  EXPORT MAPConfig
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

export(TARGETS map
  NAMESPACE MAP::
  FILE "${CMAKE_CURRENT_BINARY_DIR}/MAPConfig.cmake"
)

install(EXPORT MAPConfig
  DESTINATION "${CMAKE_INSTALL_DATADIR}/MAP/cmake"
  NAMESPACE MAP::
)
