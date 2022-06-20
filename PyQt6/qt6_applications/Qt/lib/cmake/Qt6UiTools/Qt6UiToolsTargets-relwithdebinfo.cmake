#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::UiTools" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::UiTools APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::UiTools PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtUiTools.framework/Versions/A/QtUiTools"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtUiTools.framework/Versions/A/QtUiTools"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::UiTools )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::UiTools "${_IMPORT_PREFIX}/lib/QtUiTools.framework/Versions/A/QtUiTools" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
