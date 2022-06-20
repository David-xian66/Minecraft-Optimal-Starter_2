# Make sure Qt6 is found before anything else.
set(Qt6QuickTest_FOUND FALSE)

set(__qt_use_no_default_path_for_qt_packages "NO_DEFAULT_PATH")
if(QT_DISABLE_NO_DEFAULT_PATH_IN_QT_PACKAGES)
    set(__qt_use_no_default_path_for_qt_packages "")
endif()
find_dependency(Qt6 6.1.0
    PATHS
        "${CMAKE_CURRENT_LIST_DIR}/.."
        ${_qt_additional_packages_prefix_path}
        ${_qt_additional_packages_prefix_path_env}
        ${QT_EXAMPLES_CMAKE_PREFIX_PATH}
    ${__qt_use_no_default_path_for_qt_packages}
)

# note: _third_party_deps example: "ICU\\;FALSE\\;1.0\\;i18n uc data;ZLIB\\;FALSE\\;\\;"
set(_third_party_deps "")

foreach(_target_dep ${_third_party_deps})
    list(GET _target_dep 0 pkg)
    list(GET _target_dep 1 is_optional)
    list(GET _target_dep 2 version)
    list(GET _target_dep 3 components)
    set(find_package_args "${pkg}")
    if(version)
        list(APPEND find_package_args "${version}")
    endif()
    if(components)
        string(REPLACE " " ";" components "${components}")
        list(APPEND find_package_args COMPONENTS ${components})
    endif()

    if(is_optional)
        if(${CMAKE_FIND_PACKAGE_NAME}_FIND_QUIETLY)
            list(APPEND find_package_args QUIET)
        endif()
        find_package(${find_package_args})
    else()
        find_dependency(${find_package_args})
    endif()
endforeach()

# Find Qt tool package.
set(_tool_deps "")

if(NOT "${QT_HOST_PATH}" STREQUAL "")
     # Make sure that the tools find the host tools first
     set(BACKUP_QuickTest_CMAKE_PREFIX_PATH ${CMAKE_PREFIX_PATH})
     set(BACKUP_QuickTest_CMAKE_FIND_ROOT_PATH ${CMAKE_FIND_ROOT_PATH})
     list(PREPEND CMAKE_PREFIX_PATH "${QT_HOST_PATH_CMAKE_DIR}")
     list(PREPEND CMAKE_FIND_ROOT_PATH "${QT_HOST_PATH}")
endif()

foreach(_target_dep ${_tool_deps})
    list(GET _target_dep 0 pkg)
    list(GET _target_dep 1 version)

    unset(find_package_args)
    if(${CMAKE_FIND_PACKAGE_NAME}_FIND_QUIETLY)
        list(APPEND find_package_args QUIET)
    endif()
    if(${CMAKE_FIND_PACKAGE_NAME}_FIND_REQUIRED)
        list(APPEND find_package_args REQUIRED)
    endif()
    find_package(${pkg} ${version} ${find_package_args})
    if (NOT ${pkg}_FOUND)
        if(NOT "${QT_HOST_PATH}" STREQUAL "")
             set(CMAKE_PREFIX_PATH ${BACKUP_QuickTest_CMAKE_PREFIX_PATH})
             set(CMAKE_FIND_ROOT_PATH ${BACKUP_QuickTest_CMAKE_FIND_ROOT_PATH})
        endif()
        return()
    endif()
endforeach()
if(NOT "${QT_HOST_PATH}" STREQUAL "")
     set(CMAKE_PREFIX_PATH ${BACKUP_QuickTest_CMAKE_PREFIX_PATH})
     set(CMAKE_FIND_ROOT_PATH ${BACKUP_QuickTest_CMAKE_FIND_ROOT_PATH})
endif()

# note: target_deps example: "Qt6Core\;5.12.0;Qt6Gui\;5.12.0"
set(_target_deps "Qt6Core\;6.1.0;Qt6Test\;6.1.0")
foreach(_target_dep ${_target_deps})
    list(GET _target_dep 0 pkg)
    list(GET _target_dep 1 version)

    if (NOT ${pkg}_FOUND)
        find_dependency(${pkg} ${version}
            PATHS
                "${CMAKE_CURRENT_LIST_DIR}/.."
                ${_qt_additional_packages_prefix_path}
                ${_qt_additional_packages_prefix_path_env}
                ${QT_EXAMPLES_CMAKE_PREFIX_PATH}
            ${__qt_use_no_default_path_for_qt_packages}
        )
    endif()
endforeach()

set(_Qt6QuickTest_MODULE_DEPENDENCIES "Core;Test")
set(Qt6QuickTest_FOUND TRUE)
