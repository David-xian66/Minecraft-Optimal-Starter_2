# Additional target information for Qt6QuickControls2Impl
if(NOT DEFINED QT_DEFAULT_IMPORT_CONFIGURATION)
    set(QT_DEFAULT_IMPORT_CONFIGURATION RELWITHDEBINFO)
endif()
get_target_property(_qt_imported_location Qt6::QuickControls2Impl IMPORTED_LOCATION_RELWITHDEBINFO)
get_target_property(_qt_imported_implib Qt6::QuickControls2Impl IMPORTED_IMPLIB_RELWITHDEBINFO)
get_target_property(_qt_imported_soname Qt6::QuickControls2Impl IMPORTED_SONAME_RELWITHDEBINFO)
get_target_property(_qt_imported_location_default Qt6::QuickControls2Impl IMPORTED_LOCATION_${QT_DEFAULT_IMPORT_CONFIGURATION})
get_target_property(_qt_imported_implib_default Qt6::QuickControls2Impl IMPORTED_IMPLIB_${QT_DEFAULT_IMPORT_CONFIGURATION})
get_target_property(_qt_imported_soname_default Qt6::QuickControls2Impl IMPORTED_SONAME_${QT_DEFAULT_IMPORT_CONFIGURATION})

# Import target "Qt6::QuickControls2Impl" for configuration "Release"
set_property(TARGET Qt6::QuickControls2Impl APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)

if(_qt_imported_location)
    set_property(TARGET Qt6::QuickControls2Impl PROPERTY IMPORTED_LOCATION_RELEASE "${_qt_imported_location}")
endif()
if(_qt_imported_implib)
    set_property(TARGET Qt6::QuickControls2Impl PROPERTY IMPORTED_IMPLIB_RELEASE "${_qt_imported_implib}")
endif()
if(_qt_imported_soname)
    set_property(TARGET Qt6::QuickControls2Impl PROPERTY IMPORTED_SONAME_RELEASE "${_qt_imported_soname}")
endif()

# Import target "Qt6::QuickControls2Impl" for configuration "MinSizeRel"
set_property(TARGET Qt6::QuickControls2Impl APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)

if(_qt_imported_location)
    set_property(TARGET Qt6::QuickControls2Impl PROPERTY IMPORTED_LOCATION_MINSIZEREL "${_qt_imported_location}")
endif()
if(_qt_imported_implib)
    set_property(TARGET Qt6::QuickControls2Impl PROPERTY IMPORTED_IMPLIB_MINSIZEREL "${_qt_imported_implib}")
endif()
if(_qt_imported_soname)
    set_property(TARGET Qt6::QuickControls2Impl PROPERTY IMPORTED_SONAME_MINSIZEREL "${_qt_imported_soname}")
endif()

# Default configuration
if(_qt_imported_location_default)
    set_property(TARGET Qt6::QuickControls2Impl PROPERTY IMPORTED_LOCATION "${_qt_imported_location_default}")
endif()
if(_qt_imported_implib_default)
    set_property(TARGET Qt6::QuickControls2Impl PROPERTY IMPORTED_IMPLIB "${_qt_imported_implib_default}")
endif()
if(_qt_imported_soname_default)
    set_property(TARGET Qt6::QuickControls2Impl PROPERTY IMPORTED_SONAME "${_qt_imported_soname_default}")
endif()

unset(_qt_imported_location)
unset(_qt_imported_location_default)
unset(_qt_imported_soname)
unset(_qt_imported_soname_default)
