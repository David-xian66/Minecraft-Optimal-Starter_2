set(__qt_toolchain_used_variables
    QT_CHAINLOAD_TOOLCHAIN_FILE
    QT_TOOLCHAIN_INCLUDE_FILE
    QT_TOOLCHAIN_RELOCATABLE_CMAKE_DIR
    QT_TOOLCHAIN_RELOCATABLE_PREFIX)


# Make cache variables used by this toolchain file available to the
# try_compile command that operates on sources files.
list(APPEND CMAKE_TRY_COMPILE_PLATFORM_VARIABLES ${__qt_toolchain_used_variables})
list(REMOVE_DUPLICATES CMAKE_TRY_COMPILE_PLATFORM_VARIABLES)

# Turn the environment variables that are created at the end of this
# file into proper variables. This is needed for try_compile calls
# that operate on whole projects.
if($ENV{_QT_TOOLCHAIN_VARS_INITIALIZED})
    foreach(var ${__qt_toolchain_used_variables})
        set(${var} "$ENV{_QT_TOOLCHAIN_${var}}")
    endforeach()
endif()







    set(__qt_initial_c_compiler "/usr/bin/clang")
    set(__qt_initial_cxx_compiler "/usr/bin/clang++")
    if(NOT DEFINED CMAKE_C_COMPILER AND EXISTS "${__qt_initial_c_compiler}")
        set(CMAKE_C_COMPILER "${__qt_initial_c_compiler}" CACHE STRING "")
    endif()
    if(NOT DEFINED CMAKE_CXX_COMPILER AND EXISTS "${__qt_initial_cxx_compiler}")
        set(CMAKE_CXX_COMPILER "${__qt_initial_cxx_compiler}" CACHE STRING "")
    endif()
set(CMAKE_OSX_DEPLOYMENT_TARGET "10.14" CACHE STRING "")

if(NOT "${QT_CHAINLOAD_TOOLCHAIN_FILE}" STREQUAL "")
    set(__qt_chainload_toolchain_file "${QT_CHAINLOAD_TOOLCHAIN_FILE}")
endif()
if(__qt_chainload_toolchain_file)
    get_filename_component(__qt_chainload_toolchain_file_real_path
                          "${__qt_chainload_toolchain_file}" REALPATH)
    if(__qt_chainload_toolchain_file_real_path STREQUAL CMAKE_CURRENT_LIST_FILE)
        message(FATAL_ERROR
                "Woah, the Qt toolchain file tried to include itself recusively! '${__qt_chainload_toolchain_file}' "
                "Make sure to remove qtbase/CMakeCache.txt and reconfigure qtbase with 'cmake' "
                "rather than 'qt-cmake', and then you can reconfigure your own project."
        )
    elseif(NOT EXISTS "${__qt_chainload_toolchain_file_real_path}")
        message(WARNING "The toolchain file to be chainloaded "
            "'${__qt_chainload_toolchain_file}' does not exist.")
    else()
        include("${__qt_chainload_toolchain_file}")
    endif()
    unset(__qt_chainload_toolchain_file)
endif()

# Compute dynamically the Qt installation prefix from the location of this file. This allows
# the usage of the toolchain file when the Qt installation is relocated.
get_filename_component(QT_TOOLCHAIN_RELOCATABLE_INSTALL_PREFIX
                       ${CMAKE_CURRENT_LIST_DIR}/../../../
                       ABSOLUTE)

# Compute the path to the installed Qt lib/cmake folder.
# We assume that the Qt toolchain location is inside the CMake Qt6 package, and thus the directory
# one level higher is what we're looking for.
get_filename_component(QT_TOOLCHAIN_RELOCATABLE_CMAKE_DIR "${CMAKE_CURRENT_LIST_DIR}/.." ABSOLUTE)

# There's a subdirectory check in cmake's cmFindCommon::RerootPaths() function, that doesn't handle
# the case of CMAKE_PREFIX_PATH == CMAKE_FIND_ROOT_PATH for a particular pair of entries.
# Instead of collapsing the search prefix (which is the case when one is a subdir of the other),
# it concatenates them creating an invalid path. Workaround it by setting the root path to the
# Qt install prefix, and the prefix path to the lib/cmake subdir.
list(PREPEND CMAKE_PREFIX_PATH "${QT_TOOLCHAIN_RELOCATABLE_CMAKE_DIR}")
list(PREPEND CMAKE_FIND_ROOT_PATH "${QT_TOOLCHAIN_RELOCATABLE_INSTALL_PREFIX}")


# Allow customization of the toolchain file by placing an additional file next to it.
set(__qt_toolchain_extra_file "${CMAKE_CURRENT_LIST_DIR}/qt.toolchain.extra.cmake")
if(EXISTS "${__qt_toolchain_extra_file}")
    include("${__qt_toolchain_extra_file}")
endif()

# Allow customization of the toolchain file by passing a path to an additional CMake file to be
# included.
if(QT_TOOLCHAIN_INCLUDE_FILE)
    get_filename_component(__qt_toolchain_include_file_real_path
                          "${QT_TOOLCHAIN_INCLUDE_FILE}" REALPATH)
    if(EXISTS "${__qt_toolchain_include_file_real_path}")
        include("${__qt_toolchain_include_file_real_path}")
    else()
        message(WARNING "The passed extra toolchain file to be included does not exist: "
                "${__qt_toolchain_include_file_real_path}")
    endif()
endif()

# Compile tests only see a restricted set of variables.
# All cache variables, this toolchain file uses, must be made available to compile tests,
# because this toolchain file will be included there too.
if(NOT ENV{_QT_TOOLCHAIN_VARS_INITIALIZED})
    set(ENV{_QT_TOOLCHAIN_VARS_INITIALIZED} ON)
    foreach(var ${__qt_toolchain_used_variables})
        set(ENV{_QT_TOOLCHAIN_${var}} "${${var}}")
    endforeach()
endif()
