#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::QmlWorkerScript" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::QmlWorkerScript APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::QmlWorkerScript PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtQmlWorkerScript.framework/Versions/A/QtQmlWorkerScript"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtQmlWorkerScript.framework/Versions/A/QtQmlWorkerScript"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::QmlWorkerScript )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::QmlWorkerScript "${_IMPORT_PREFIX}/lib/QtQmlWorkerScript.framework/Versions/A/QtQmlWorkerScript" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
