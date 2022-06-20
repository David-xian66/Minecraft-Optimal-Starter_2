if(NOT QT_NO_CREATE_TARGETS AND
   NOT "ON" AND              # Only needed if Qt was built statically
   CMAKE_VERSION VERSION_GREATER_EQUAL 3.18)  # Finalizers require cmake_language(CALL)
    set(target Qt6::Qml)
    get_property(aliased_target TARGET ${target} PROPERTY ALIASED_TARGET)
    if(aliased_target)
        set(target "${aliased_target}")
    endif()
    set_property(TARGET ${target} PROPERTY
        INTERFACE_QT_EXECUTABLE_FINALIZERS
        qt6_import_qml_plugins
    )
endif()
