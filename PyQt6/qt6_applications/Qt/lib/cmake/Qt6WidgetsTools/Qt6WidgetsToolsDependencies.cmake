# Find "ModuleTools" dependencies, which are other ModuleTools packages.
set(Qt6WidgetsTools_FOUND FALSE)
set(_tool_deps "Qt6CoreTools\;6.1.0;Qt6GuiTools\;6.1.0")
foreach(_target_dep ${_tool_deps})
    list(GET _target_dep 0 pkg)
    list(GET _target_dep 1 version)

    if (NOT ${pkg}_FOUND)
        find_dependency(${pkg} ${version})
    endif()
endforeach()

set(Qt6WidgetsTools_FOUND TRUE)
