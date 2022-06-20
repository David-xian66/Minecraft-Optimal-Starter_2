foreach(__qt_tool qdbuscpp2xml;qdbusxml2cpp)
    if(NOT TARGET Qt::${__qt_tool} AND TARGET Qt6::${__qt_tool})
        add_executable(Qt::${__qt_tool} IMPORTED)

        # Check all the usual imported location properties to find one that contains a path.
        foreach(__qt_imported_location_config
                IMPORTED_LOCATION
                IMPORTED_LOCATION_RELEASE
                IMPORTED_LOCATION_RELWITHDEBINFO
                IMPORTED_LOCATION_MINSIZEREL
                IMPORTED_LOCATION_DEBUG)

            get_target_property(__qt_imported_location
                                Qt6::${__qt_tool} ${__qt_imported_location_config})
            if(__qt_imported_location AND EXISTS "${__qt_imported_location}")
                break()
            endif()
        endforeach()

        set_target_properties(Qt::${__qt_tool}
                              PROPERTIES IMPORTED_LOCATION "${__qt_imported_location}")
    endif()
endforeach()
