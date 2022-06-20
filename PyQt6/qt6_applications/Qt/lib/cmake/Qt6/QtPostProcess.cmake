include(QtPostProcessHelpers)

qt_internal_create_depends_files()
qt_generate_build_internals_extra_cmake_code()
qt_internal_create_plugins_files()
qt_internal_create_config_file_for_standalone_tests()

# Needs to run after qt_internal_create_depends_files.
qt_create_tools_config_files()

if (ANDROID)
    qt_modules_process_android_dependencies()
endif()

qt_internal_install_prl_files()
qt_internal_generate_user_facing_tools_info()
