#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::Qml" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::Qml APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::Qml PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtQml.framework/Versions/A/QtQml"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtQml.framework/Versions/A/QtQml"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::Qml )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::Qml "${_IMPORT_PREFIX}/lib/QtQml.framework/Versions/A/QtQml" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
