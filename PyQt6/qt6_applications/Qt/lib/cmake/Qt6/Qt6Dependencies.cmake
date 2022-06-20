set(Qt6_DEPENDENCIES_FOUND FALSE)

# note: _third_party_deps example: "ICU\\;FALSE\\;1.0\\;i18n uc data;ZLIB\\;FALSE\\;\\;"
set(_third_party_deps "Threads\;FALSE\;\;")

if(NOT QT_NO_THREADS_PREFER_PTHREAD_FLAG)
    set(THREADS_PREFER_PTHREAD_FLAG TRUE)
endif()

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

    # Already build an error message, because find_dependency calls return() on failure.
    set(__Qt6_message "\nPackage: ${pkg}")
    if(version)
        string(APPEND __Qt6_message "\nVersion: ${version}")
    endif()
    if(components)
        string(APPEND __Qt6_message "\nComponents: ${components}")
    endif()
    set(Qt6_DEPENDENCY_NOT_FOUND_MESSAGE
        "${__Qt6_message}")

    if(is_optional)
        if(${CMAKE_FIND_PACKAGE_NAME}_FIND_QUIETLY)
            list(APPEND find_package_args QUIET)
        endif()
        find_package(${find_package_args})
    else()
        find_dependency(${find_package_args})
    endif()
endforeach()

set(Qt6_DEPENDENCIES_FOUND TRUE)
unset(Qt6_DEPENDENCY_NOT_FOUND_MESSAGE)
