#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::Xml" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::Xml APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::Xml PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtXml.framework/Versions/A/QtXml"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtXml.framework/Versions/A/QtXml"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::Xml )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::Xml "${_IMPORT_PREFIX}/lib/QtXml.framework/Versions/A/QtXml" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
