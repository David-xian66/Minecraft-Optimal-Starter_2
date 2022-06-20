# Given "/usr/lib/x86_64-linux-gnu/libcups.so"
# Returns "cups" or an empty string if the file is not an absolute library path.
# Aka it strips the "lib" prefix, the .so extension and the base path.
function(qt_get_library_name_without_prefix_and_suffix out_var file_path)
    set(out_value "")
    if(IS_ABSOLUTE "${file_path}")
        get_filename_component(basename "${file_path}" NAME_WE)
        get_filename_component(ext "${file_path}" EXT)
        foreach(libsuffix ${LIBRARY_SUFFIXES})
            # Handle weird prefix extensions like in the case of
            # "/usr/lib/x86_64-linux-gnu/libglib-2.0.so"
            # it's ".0.so".
            if(ext MATCHES "^(\\.[0-9]+)*${libsuffix}(\\.[0-9]+)*")
                set(is_linkable_library TRUE)
                set(weird_numbered_extension "${CMAKE_MATCH_1}")
                break()
            endif()
        endforeach()
        if(is_linkable_library)
            set(out_value "${basename}")
            if(LIBRARY_PREFIXES)
                foreach(libprefix ${LIBRARY_PREFIXES})
                    # Strip any library prefix like "lib" for a library that we will use with a link
                    # flag.
                    if(libprefix AND out_value MATCHES "^${libprefix}(.+)")
                        set(out_value "${CMAKE_MATCH_1}")
                        break()
                    endif()
                endforeach()
            endif()
            if(weird_numbered_extension)
                set(out_value "${out_value}${weird_numbered_extension}")
            endif()
        endif()
    endif()

    # Reverse the dependency order to be in sync with what qmake generated .pri files
    # have.
    list(REVERSE out_list)

    set(${out_var} "${out_value}" PARENT_SCOPE)
endfunction()

# Given "/usr/lib/x86_64-linux-gnu/libcups.so"
# Returns "-lcups" or an empty string if the file is not an absolute library path.
function(qt_get_library_with_link_flag out_var file_path)
    qt_get_library_name_without_prefix_and_suffix(lib_name "${file_path}")

    set(out_value "")
    if(lib_name)
        set(out_value "${lib_name}")
        if(LINK_LIBRARY_FLAG)
            string(PREPEND out_value "${LINK_LIBRARY_FLAG}")
        endif()
    endif()

    set(${out_var} "${out_value}" PARENT_SCOPE)
endfunction()

# Given a list of potential library paths, returns a transformed list where absolute library paths
# are replaced with library link flags.
function(qt_transform_absolute_library_paths_to_link_flags out_var library_path_list)
    set(out_list "")
    foreach(library_path ${library_path_list})
        qt_get_library_with_link_flag(lib_name_with_link_flag "${library_path}")
        if(lib_name_with_link_flag)
            list(APPEND out_list "${lib_name_with_link_flag}")
        else()
            list(APPEND out_list "${library_path}")
        endif()
    endforeach()
    set(${out_var} "${out_list}" PARENT_SCOPE)
endfunction()

function(qt_strip_library_version_suffix out_var file_path)
    get_filename_component(dir "${file_path}" DIRECTORY)
    get_filename_component(basename "${file_path}" NAME_WE)
    get_filename_component(ext "${file_path}" EXT)
    foreach(libsuffix ${LIBRARY_SUFFIXES})
        if(ext MATCHES "^${libsuffix}(\\.[0-9]+)+")
            set(ext ${libsuffix})
            break()
        endif()
    endforeach()
    set(final_value "${basename}${ext}")
    if(dir)
        set(final_value "${dir}/${final_value}")
    endif()
    set(${out_var} "${final_value}" PARENT_SCOPE)
endfunction()

# Checks if `input_path` is relative to at least one path given in the list of `qt_lib_paths`.
# Sets TRUE or FALSE in `out_var_is_relative`.
# Assigns the relative path to `out_var_relative_path` if the path is relative, otherwise assigns
# the original path.
function(qt_internal_path_is_relative_to_qt_lib_path
        input_path qt_lib_paths out_var_is_relative out_var_relative_path)
    set(is_relative "FALSE")
    set(relative_path_value "${input_path}")

    foreach(qt_lib_path ${qt_lib_paths})
        file(RELATIVE_PATH relative_path "${qt_lib_path}" "${input_path}")
        if(IS_ABSOLUTE "${relative_path}" OR (relative_path MATCHES "^\\.\\."))
            set(is_relative "FALSE")
        else()
            set(is_relative "TRUE")
            set(relative_path_value "${relative_path}")
            break()
        endif()
    endforeach()
    set(${out_var_is_relative} "${is_relative}" PARENT_SCOPE)
    set(${out_var_relative_path} "${relative_path_value}" PARENT_SCOPE)
endfunction()
