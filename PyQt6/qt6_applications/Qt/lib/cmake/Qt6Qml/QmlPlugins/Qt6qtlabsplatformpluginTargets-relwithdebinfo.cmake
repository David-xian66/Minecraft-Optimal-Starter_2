#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::qtlabsplatformplugin" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::qtlabsplatformplugin APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::qtlabsplatformplugin PROPERTIES
  IMPORTED_COMMON_LANGUAGE_RUNTIME_RELWITHDEBINFO ""
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/./qml/Qt/labs/platform/libqtlabsplatformplugin.dylib"
  IMPORTED_NO_SONAME_RELWITHDEBINFO "TRUE"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::qtlabsplatformplugin )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::qtlabsplatformplugin "${_IMPORT_PREFIX}/./qml/Qt/labs/platform/libqtlabsplatformplugin.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
