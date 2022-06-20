#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::Network" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::Network APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::Network PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtNetwork.framework/Versions/A/QtNetwork"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtNetwork.framework/Versions/A/QtNetwork"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::Network )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::Network "${_IMPORT_PREFIX}/lib/QtNetwork.framework/Versions/A/QtNetwork" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
