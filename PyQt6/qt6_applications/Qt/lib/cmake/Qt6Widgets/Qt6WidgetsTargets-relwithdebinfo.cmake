#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::Widgets" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::Widgets APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::Widgets PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtWidgets.framework/Versions/A/QtWidgets"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtWidgets.framework/Versions/A/QtWidgets"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::Widgets )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::Widgets "${_IMPORT_PREFIX}/lib/QtWidgets.framework/Versions/A/QtWidgets" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
