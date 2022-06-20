#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::LabsFolderListModel" for configuration "RelWithDebInfo"
set_property(TARGET Qt6::LabsFolderListModel APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(Qt6::LabsFolderListModel PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/QtLabsFolderListModel.framework/Versions/A/QtLabsFolderListModel"
  IMPORTED_SONAME_RELWITHDEBINFO "@rpath/QtLabsFolderListModel.framework/Versions/A/QtLabsFolderListModel"
  )

list(APPEND _IMPORT_CHECK_TARGETS Qt6::LabsFolderListModel )
list(APPEND _IMPORT_CHECK_FILES_FOR_Qt6::LabsFolderListModel "${_IMPORT_PREFIX}/lib/QtLabsFolderListModel.framework/Versions/A/QtLabsFolderListModel" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
