#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::OpenGLWidgets" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::OpenGLWidgets APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::OpenGLWidgets PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtOpenGLWidgets.framework/Versions/A/QtOpenGLWidgets"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtOpenGLWidgets.framework/Versions/A/QtOpenGLWidgets"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::OpenGLWidgets )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::OpenGLWidgets "${_IMPORT_PREFIX}/lib/QtOpenGLWidgets.framework/Versions/A/QtOpenGLWidgets" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
