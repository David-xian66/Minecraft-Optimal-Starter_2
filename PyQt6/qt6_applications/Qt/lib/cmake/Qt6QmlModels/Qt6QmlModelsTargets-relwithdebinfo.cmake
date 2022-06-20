#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::QmlModels" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::QmlModels APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::QmlModels PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtQmlModels.framework/Versions/A/QtQmlModels"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtQmlModels.framework/Versions/A/QtQmlModels"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::QmlModels )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::QmlModels "${_IMPORT_PREFIX}/lib/QtQmlModels.framework/Versions/A/QtQmlModels" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
