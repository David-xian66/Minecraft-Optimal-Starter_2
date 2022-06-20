#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::OpenGL" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::OpenGL APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::OpenGL PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtOpenGL.framework/Versions/A/QtOpenGL"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtOpenGL.framework/Versions/A/QtOpenGL"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::OpenGL )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::OpenGL "${_IMPORT_PREFIX}/lib/QtOpenGL.framework/Versions/A/QtOpenGL" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
