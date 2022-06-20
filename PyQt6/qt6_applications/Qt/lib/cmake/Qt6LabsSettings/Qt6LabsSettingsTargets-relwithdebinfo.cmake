#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::LabsSettings" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::LabsSettings APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::LabsSettings PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtLabsSettings.framework/Versions/A/QtLabsSettings"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtLabsSettings.framework/Versions/A/QtLabsSettings"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::LabsSettings )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::LabsSettings "${_IMPORT_PREFIX}/lib/QtLabsSettings.framework/Versions/A/QtLabsSettings" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
