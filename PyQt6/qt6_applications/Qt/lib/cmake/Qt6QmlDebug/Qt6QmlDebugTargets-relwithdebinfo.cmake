#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::QmlDebug" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::QmlDebug APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::QmlDebug PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELWITHDEBINFO "CXX"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libQt6QmlDebug.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::QmlDebug )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::QmlDebug "${_IMPORT_PREFIX}/lib/libQt6QmlDebug.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
