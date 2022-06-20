#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::LabsQmlModels" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::LabsQmlModels APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::LabsQmlModels PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtLabsQmlModels.framework/Versions/A/QtLabsQmlModels"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtLabsQmlModels.framework/Versions/A/QtLabsQmlModels"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::LabsQmlModels )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::LabsQmlModels "${_IMPORT_PREFIX}/lib/QtLabsQmlModels.framework/Versions/A/QtLabsQmlModels" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
