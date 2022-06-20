#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::LabsWavefrontMesh" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::LabsWavefrontMesh APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::LabsWavefrontMesh PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtLabsWavefrontMesh.framework/Versions/A/QtLabsWavefrontMesh"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtLabsWavefrontMesh.framework/Versions/A/QtLabsWavefrontMesh"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::LabsWavefrontMesh )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::LabsWavefrontMesh "${_IMPORT_PREFIX}/lib/QtLabsWavefrontMesh.framework/Versions/A/QtLabsWavefrontMesh" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
