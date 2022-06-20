#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::PacketProtocol" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::PacketProtocol APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::PacketProtocol PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELWITHDEBINFO "CXX"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libQt6PacketProtocol.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::PacketProtocol )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::PacketProtocol "${_IMPORT_PREFIX}/lib/libQt6PacketProtocol.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
