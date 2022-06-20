#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::qtquickcontrols2fusionstyleplugin" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::qtquickcontrols2fusionstyleplugin APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::qtquickcontrols2fusionstyleplugin PROPERTIES
  IMPORTED_COMMON_LANGUAGE_RUNTIME_RELWITHDEBINFO ""
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/./qml/QtQuick/Controls/Fusion/libqtquickcontrols2fusionstyleplugin.dylib"
  IMPORTED_NO_SONAME_RELWITHDEBINFO "TRUE"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::qtquickcontrols2fusionstyleplugin )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::qtquickcontrols2fusionstyleplugin "${_IMPORT_PREFIX}/./qml/QtQuick/Controls/Fusion/libqtquickcontrols2fusionstyleplugin.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
