#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::moc" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::moc APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::moc PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/./libexec/moc"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::moc )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::moc "${_IMPORT_PREFIX}/./libexec/moc" )

# Import target "Qt6::rcc" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::rcc APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::rcc PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/./libexec/rcc"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::rcc )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::rcc "${_IMPORT_PREFIX}/./libexec/rcc" )

# Import target "Qt6::tracegen" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::tracegen APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::tracegen PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/./libexec/tracegen"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::tracegen )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::tracegen "${_IMPORT_PREFIX}/./libexec/tracegen" )

# Import target "Qt6::cmake_automoc_parser" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::cmake_automoc_parser APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::cmake_automoc_parser PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/./libexec/cmake_automoc_parser"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::cmake_automoc_parser )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::cmake_automoc_parser "${_IMPORT_PREFIX}/./libexec/cmake_automoc_parser" )

# Import target "Qt6::qlalr" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::qlalr APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::qlalr PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/./libexec/qlalr"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::qlalr )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::qlalr "${_IMPORT_PREFIX}/./libexec/qlalr" )

# Import target "Qt6::qmake" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::qmake APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::qmake PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/bin/qmake"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::qmake )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::qmake "${_IMPORT_PREFIX}/bin/qmake" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
