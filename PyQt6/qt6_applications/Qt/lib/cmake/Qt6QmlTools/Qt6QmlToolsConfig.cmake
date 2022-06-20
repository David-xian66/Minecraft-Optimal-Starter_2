
####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was QtModuleToolsConfig.cmake.in                            ########

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

include(CMakeFindDependencyMacro)

if (NOT QT_NO_CREATE_TARGETS)
    # Find required dependencies, if any.
    if(EXISTS "${CMAKE_CURRENT_LIST_DIR}/Qt6QmlToolsDependencies.cmake")
        include("${CMAKE_CURRENT_LIST_DIR}/Qt6QmlToolsDependencies.cmake")
    endif()

    include("${CMAKE_CURRENT_LIST_DIR}/Qt6QmlToolsTargets.cmake")
    include("${CMAKE_CURRENT_LIST_DIR}/Qt6QmlToolsAdditionalTargetInfo.cmake")
    if(NOT QT_NO_CREATE_VERSIONLESS_TARGETS)
        include("${CMAKE_CURRENT_LIST_DIR}/Qt6QmlToolsVersionlessTargets.cmake")
    endif()
endif()

foreach(extra_cmake_include )
    include("${CMAKE_CURRENT_LIST_DIR}/${extra_cmake_include}")
endforeach()


if (NOT QT_NO_CREATE_TARGETS)
    get_property(is_global TARGET Qt6::qmltyperegistrar PROPERTY IMPORTED_GLOBAL)
    if(NOT is_global)
        set_property(TARGET Qt6::qmltyperegistrar PROPERTY IMPORTED_GLOBAL TRUE)
    endif()
endif()

if (NOT QT_NO_CREATE_TARGETS)
    get_property(is_global TARGET Qt6::qmlcachegen PROPERTY IMPORTED_GLOBAL)
    if(NOT is_global)
        set_property(TARGET Qt6::qmlcachegen PROPERTY IMPORTED_GLOBAL TRUE)
    endif()
endif()

if (NOT QT_NO_CREATE_TARGETS)
    get_property(is_global TARGET Qt6::qmllint PROPERTY IMPORTED_GLOBAL)
    if(NOT is_global)
        set_property(TARGET Qt6::qmllint PROPERTY IMPORTED_GLOBAL TRUE)
    endif()
endif()

if (NOT QT_NO_CREATE_TARGETS)
    get_property(is_global TARGET Qt6::qmlimportscanner PROPERTY IMPORTED_GLOBAL)
    if(NOT is_global)
        set_property(TARGET Qt6::qmlimportscanner PROPERTY IMPORTED_GLOBAL TRUE)
    endif()
endif()

if (NOT QT_NO_CREATE_TARGETS)
    get_property(is_global TARGET Qt6::qmlformat PROPERTY IMPORTED_GLOBAL)
    if(NOT is_global)
        set_property(TARGET Qt6::qmlformat PROPERTY IMPORTED_GLOBAL TRUE)
    endif()
endif()

if (NOT QT_NO_CREATE_TARGETS)
    get_property(is_global TARGET Qt6::qml PROPERTY IMPORTED_GLOBAL)
    if(NOT is_global)
        set_property(TARGET Qt6::qml PROPERTY IMPORTED_GLOBAL TRUE)
    endif()
endif()

if (NOT QT_NO_CREATE_TARGETS)
    get_property(is_global TARGET Qt6::qmlprofiler PROPERTY IMPORTED_GLOBAL)
    if(NOT is_global)
        set_property(TARGET Qt6::qmlprofiler PROPERTY IMPORTED_GLOBAL TRUE)
    endif()
endif()

if (NOT QT_NO_CREATE_TARGETS)
    get_property(is_global TARGET Qt6::qmlpreview PROPERTY IMPORTED_GLOBAL)
    if(NOT is_global)
        set_property(TARGET Qt6::qmlpreview PROPERTY IMPORTED_GLOBAL TRUE)
    endif()
endif()

if (NOT QT_NO_CREATE_TARGETS)
    get_property(is_global TARGET Qt6::qmlscene PROPERTY IMPORTED_GLOBAL)
    if(NOT is_global)
        set_property(TARGET Qt6::qmlscene PROPERTY IMPORTED_GLOBAL TRUE)
    endif()
endif()

if (NOT QT_NO_CREATE_TARGETS)
    get_property(is_global TARGET Qt6::qmltime PROPERTY IMPORTED_GLOBAL)
    if(NOT is_global)
        set_property(TARGET Qt6::qmltime PROPERTY IMPORTED_GLOBAL TRUE)
    endif()
endif()

if (NOT QT_NO_CREATE_TARGETS)
    get_property(is_global TARGET Qt6::qmlplugindump PROPERTY IMPORTED_GLOBAL)
    if(NOT is_global)
        set_property(TARGET Qt6::qmlplugindump PROPERTY IMPORTED_GLOBAL TRUE)
    endif()
endif()

if (NOT QT_NO_CREATE_TARGETS)
    get_property(is_global TARGET Qt6::qmltestrunner PROPERTY IMPORTED_GLOBAL)
    if(NOT is_global)
        set_property(TARGET Qt6::qmltestrunner PROPERTY IMPORTED_GLOBAL TRUE)
    endif()
endif()
set(Qt6QmlTools_TARGETS "Qt6::qmltyperegistrar;Qt6::qmlcachegen;Qt6::qmllint;Qt6::qmlimportscanner;Qt6::qmlformat;Qt6::qml;Qt6::qmlprofiler;Qt6::qmlpreview;Qt6::qmlscene;Qt6::qmltime;Qt6::qmlplugindump;Qt6::qmltestrunner")
