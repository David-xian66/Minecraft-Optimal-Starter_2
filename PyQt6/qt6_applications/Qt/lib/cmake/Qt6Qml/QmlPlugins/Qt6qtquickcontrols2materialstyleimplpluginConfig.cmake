include_guard(DIRECTORY)


####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was QtPluginConfig.cmake.in                            ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../../" ABSOLUTE)

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

get_filename_component(_import_prefix "${CMAKE_CURRENT_LIST_FILE}" PATH)
get_filename_component(_import_prefix "${_import_prefix}" REALPATH)

if (NOT QT_NO_CREATE_TARGETS)
    # Find required dependencies, if any.
    if(EXISTS "${CMAKE_CURRENT_LIST_DIR}/Qt6qtquickcontrols2materialstyleimplpluginDependencies.cmake")
        include("${CMAKE_CURRENT_LIST_DIR}/Qt6qtquickcontrols2materialstyleimplpluginDependencies.cmake")
    endif()

    include("${CMAKE_CURRENT_LIST_DIR}/Qt6qtquickcontrols2materialstyleimplpluginTargets.cmake")
    include("${CMAKE_CURRENT_LIST_DIR}/Qt6qtquickcontrols2materialstyleimplpluginAdditionalTargetInfo.cmake")
endif()
