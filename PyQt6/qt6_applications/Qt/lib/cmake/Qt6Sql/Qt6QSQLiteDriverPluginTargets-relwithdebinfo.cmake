#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::QSQLiteDriverPlugin" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::QSQLiteDriverPlugin APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::QSQLiteDriverPlugin PROPERTIES
  IMPORTED_COMMON_LANGUAGE_RUNTIME_RELWITHDEBINFO ""
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/./plugins/sqldrivers/libqsqlite.dylib"
  IMPORTED_NO_SONAME_RELWITHDEBINFO "TRUE"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::QSQLiteDriverPlugin )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::QSQLiteDriverPlugin "${_IMPORT_PREFIX}/./plugins/sqldrivers/libqsqlite.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
