#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::QuickWidgets" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::QuickWidgets APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::QuickWidgets PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtQuickWidgets.framework/Versions/A/QtQuickWidgets"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtQuickWidgets.framework/Versions/A/QtQuickWidgets"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::QuickWidgets )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::QuickWidgets "${_IMPORT_PREFIX}/lib/QtQuickWidgets.framework/Versions/A/QtQuickWidgets" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
