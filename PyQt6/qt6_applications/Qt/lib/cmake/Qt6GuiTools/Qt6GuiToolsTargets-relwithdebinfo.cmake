#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::qvkgen" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::qvkgen APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::qvkgen PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/./libexec/qvkgen"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::qvkgen )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::qvkgen "${_IMPORT_PREFIX}/./libexec/qvkgen" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
