#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::Svg" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::Svg APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::Svg PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtSvg.framework/Versions/A/QtSvg"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtSvg.framework/Versions/A/QtSvg"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::Svg )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::Svg "${_IMPORT_PREFIX}/lib/QtSvg.framework/Versions/A/QtSvg" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
