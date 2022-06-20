#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::Gui" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::Gui APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::Gui PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELWITHDEBINFO "Qt6::DBus"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtGui.framework/Versions/A/QtGui"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtGui.framework/Versions/A/QtGui"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::Gui )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::Gui "${_IMPORT_PREFIX}/lib/QtGui.framework/Versions/A/QtGui" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
