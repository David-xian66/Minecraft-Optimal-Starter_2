#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::Sql" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::Sql APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::Sql PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtSql.framework/Versions/A/QtSql"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtSql.framework/Versions/A/QtSql"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::Sql )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::Sql "${_IMPORT_PREFIX}/lib/QtSql.framework/Versions/A/QtSql" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
