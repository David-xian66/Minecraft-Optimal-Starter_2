#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::DBus" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::DBus APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::DBus PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtDBus.framework/Versions/A/QtDBus"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtDBus.framework/Versions/A/QtDBus"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::DBus )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::DBus "${_IMPORT_PREFIX}/lib/QtDBus.framework/Versions/A/QtDBus" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
