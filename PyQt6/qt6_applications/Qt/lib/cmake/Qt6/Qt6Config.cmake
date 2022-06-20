
####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was QtConfig.cmake.in                            ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../" ABSOLUTE)

macro(set_and_check _var _file)
  set(${_var} "${_file}")
  if(NOT EXISTS "${_file}")
    message(FATAL_ERROR "File or directory ${_file} referenced by variable ${_var} does not exist !")
  endif()
endmacro()

macro(check_required_components _NAME)
  foreach(comp ${${_NAME}_FIND_COMPONENTS})
    if(NOT ${_NAME}_${comp}_FOUND)
      if(${_NAME}_FIND_REQUIRED_${comp})
        set(${_NAME}_FOUND FALSE)
      endif()
    endif()
  endforeach()
endmacro()

####################################################################################

cmake_minimum_required(VERSION 3.14...3.19)

get_filename_component(_qt_cmake_dir "${CMAKE_CURRENT_LIST_DIR}/.." ABSOLUTE)
set(_qt_6_config_cmake_dir "${CMAKE_CURRENT_LIST_DIR}")

if (NOT QT_NO_CREATE_TARGETS)
    include("${CMAKE_CURRENT_LIST_DIR}/Qt6Targets.cmake")
    if(NOT QT_NO_CREATE_VERSIONLESS_TARGETS)
        include("${CMAKE_CURRENT_LIST_DIR}/Qt6VersionlessTargets.cmake")
    endif()
else()
    # For examples using `find_package(...)` inside their CMakeLists.txt files:
    # Make CMake's AUTOGEN detect this Qt version properly
    set_directory_properties(PROPERTIES
                             QT_VERSION_MAJOR 6
                             QT_VERSION_MINOR 1
                             QT_VERSION_PATCH 0)
endif()

if(NOT "${QT_HOST_PATH}" STREQUAL "")
    find_package(Qt6HostInfo
                 CONFIG
                 REQUIRED
                 PATHS "${QT_HOST_PATH}"
                       "${QT_HOST_PATH_CMAKE_DIR}"
                 NO_CMAKE_FIND_ROOT_PATH
                 NO_DEFAULT_PATH)
endif()

# if (NOT Qt6_FIND_COMPONENTS)
#     set(Qt6_NOT_FOUND_MESSAGE "The Qt package requires at least one component")
#     set(Qt6_FOUND False)
#     return()
# endif()

get_filename_component(_qt_import_prefix "${CMAKE_CURRENT_LIST_FILE}" PATH)
get_filename_component(_qt_import_prefix "${_qt_import_prefix}" REALPATH)
list(APPEND CMAKE_MODULE_PATH "${_qt_import_prefix}")
list(APPEND CMAKE_MODULE_PATH "${_qt_import_prefix}/3rdparty/extra-cmake-modules/find-modules")
list(APPEND CMAKE_MODULE_PATH "${_qt_import_prefix}/3rdparty/kwin")

if(APPLE AND (NOT CMAKE_SYSTEM_NAME OR CMAKE_SYSTEM_NAME STREQUAL "Darwin"))
    # Add module directory to pick up custom Info.plist template for macOS
    list(APPEND CMAKE_MODULE_PATH "${_qt_import_prefix}/macos")
endif()

set(QT_ADDITIONAL_PACKAGES_PREFIX_PATH "" CACHE STRING "Additional directories where find(Qt6 ...) components are searched")
file(TO_CMAKE_PATH "${QT_ADDITIONAL_PACKAGES_PREFIX_PATH}" _qt_additional_packages_prefix_path)
file(TO_CMAKE_PATH "$ENV{QT_ADDITIONAL_PACKAGES_PREFIX_PATH}" _qt_additional_packages_prefix_path_env)

# Find required dependencies, if any.
include(CMakeFindDependencyMacro)
if(EXISTS "${CMAKE_CURRENT_LIST_DIR}/Qt6Dependencies.cmake")
    include("${CMAKE_CURRENT_LIST_DIR}/Qt6Dependencies.cmake")
    if(NOT Qt6_DEPENDENCIES_FOUND)
        set(Qt6_FOUND FALSE)
        message(FATAL_ERROR "Failed to find Qt Platform dependency: "
            "${Qt6_DEPENDENCY_NOT_FOUND_MESSAGE}")
    endif()
endif()

set(__qt_use_no_default_path_for_qt_packages "NO_DEFAULT_PATH")
if(QT_DISABLE_NO_DEFAULT_PATH_IN_QT_PACKAGES)
    set(__qt_use_no_default_path_for_qt_packages "")
endif()

foreach(module ${Qt6_FIND_COMPONENTS})
    find_package(Qt6${module}
        ${_Qt6_FIND_PARTS_QUIET}
        ${_Qt6_FIND_PARTS_REQUIRED}
        PATHS
            ${_qt_cmake_dir}
            ${_qt_additional_packages_prefix_path}
            ${_qt_additional_packages_prefix_path_env}
            ${QT_EXAMPLES_CMAKE_PREFIX_PATH}
        ${__qt_use_no_default_path_for_qt_packages}
    )
    if (NOT Qt6${module}_FOUND)
        string(CONFIGURE ${_qt5_module_location_template} _expected_module_location @ONLY)

        if (Qt6_FIND_REQUIRED_${module})
            set(_Qt_NOTFOUND_MESSAGE "${_Qt_NOTFOUND_MESSAGE}Failed to find Qt component \"${module}\" config file at                                       \"${_expected_module_location}\"\n")
        elseif(NOT Qt6_FIND_QUIETLY)
            message(WARNING "Failed to find Qt component \"${module}\" config file at \"${_expected_module_location}\"")
        endif()

        unset(_expected_module_location)
    endif()
endforeach()

if (_Qt_NOTFOUND_MESSAGE)
    set(Qt6_NOT_FOUND_MESSAGE "${_Qt_NOTFOUND_MESSAGE}")
    set(Qt6_FOUND False)
endif()
