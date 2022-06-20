#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::QuickTest" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::QuickTest APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::QuickTest PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELWITHDEBINFO "Qt6::Quick"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtQuickTest.framework/Versions/A/QtQuickTest"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtQuickTest.framework/Versions/A/QtQuickTest"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::QuickTest )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::QuickTest "${_IMPORT_PREFIX}/lib/QtQuickTest.framework/Versions/A/QtQuickTest" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
