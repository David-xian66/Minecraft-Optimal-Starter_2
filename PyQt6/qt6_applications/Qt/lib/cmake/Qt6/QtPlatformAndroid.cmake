#
# Self contained Platform Settings for Android
#
# Note: This file is used by the internal builds.
#

#
# Variables:
#   QT_ANDROID_JAR
#       Location of the adroid sdk jar for java code
#   QT_ANDROID_API_VERSION
#       Android API version
#

if (NOT DEFINED ANDROID_SDK_ROOT)
    message(FATAL_ERROR "Please provide the location of the Android SDK directory via -DANDROID_SDK_ROOT=<path to Android SDK>")
endif()

if (NOT IS_DIRECTORY "${ANDROID_SDK_ROOT}")
    message(FATAL_ERROR "Could not find ANDROID_SDK_ROOT or path is not a directory: ${ANDROID_SDK_ROOT}")
endif()

# Get the Android SDK jar for an API version other than the one specified with
# QT_ANDROID_API_VERSION.
function(qt_get_android_sdk_jar_for_api api out_jar_location)
    set(jar_location "${ANDROID_SDK_ROOT}/platforms/${api}/android.jar")
    if (NOT EXISTS "${jar_location}")
        message(WARNING "Could not locate Android SDK jar for api '${api}', defaulting to ${QT_ANDROID_API_VERSION}")
        set(${out_jar_location} ${QT_ANDROID_JAR} PARENT_SCOPE)
    else()
        set(${out_jar_location} ${jar_location} PARENT_SCOPE)
    endif()
endfunction()

# Minimum recommend android SDK api version
set(QT_ANDROID_API_VERSION "android-29")

# Locate android.jar
set(QT_ANDROID_JAR "${ANDROID_SDK_ROOT}/platforms/${QT_ANDROID_API_VERSION}/android.jar")
if(NOT EXISTS "${QT_ANDROID_JAR}")
    # Locate the highest available platform
    file(GLOB android_platforms
        LIST_DIRECTORIES true
        RELATIVE "${ANDROID_SDK_ROOT}/platforms"
        "${ANDROID_SDK_ROOT}/platforms/*")
    # If list is not empty
    if(android_platforms)
        list(SORT android_platforms)
        list(REVERSE android_platforms)
        list(GET android_platforms 0 android_platform_latest)
        set(QT_ANDROID_API_VERSION ${android_platform_latest})
        set(QT_ANDROID_JAR "${ANDROID_SDK_ROOT}/platforms/${QT_ANDROID_API_VERSION}/android.jar")
    endif()
endif()

if(NOT EXISTS "${QT_ANDROID_JAR}")
    message(FATAL_ERROR "No suitable Android SDK platform found. Minimum version is ${QT_ANDROID_API_VERSION}")
endif()

message(STATUS "Using Android SDK API ${QT_ANDROID_API_VERSION} from ${ANDROID_SDK_ROOT}/platforms")

# Locate Java
include(UseJava)

# Find JDK 8.0
find_package(Java 1.8 COMPONENTS Development REQUIRED)

# Ensure we are using the shared version of libc++
if(NOT ANDROID_STL STREQUAL c++_shared)
    message(FATAL_ERROR "The Qt libraries on Android only supports the shared library configuration of stl. Please use -DANDROID_STL=\"c++_shared\" as configuration argument.")
endif()

# Target properties required for android deploy tool
define_property(TARGET
    PROPERTY
        QT_ANDROID_DEPLOYMENT_DEPENDENCIES
    BRIEF_DOCS
        "Specify additional plugins that need to be deployed with the current android application"
    FULL_DOCS
        "By default, androiddeployqt will detect the dependencies of your application. But since run-time usage of plugins cannot be detected, there could be false positives, as your application will depend on any plugins that are potential dependencies. If you want to minimize the size of your APK, it's possible to override the automatic detection using the ANDROID_DEPLOYMENT_DEPENDENCIES variable. This should contain a list of all Qt files which need to be included, with paths relative to the Qt install root. Note that only the Qt files specified here will be included. Failing to include the correct files can result in crashes. It's also important to make sure the files are listed in the correct loading order. This variable provides a way to override the automatic detection entirely, so if a library is listed before its dependencies, it will fail to load on some devices."
)

define_property(TARGET
    PROPERTY
        QT_ANDROID_EXTRA_LIBS
    BRIEF_DOCS
        "A list of external libraries that will be copied into your application's library folder and loaded on start-up."
    FULL_DOCS
    "A list of external libraries that will be copied into your application's library folder and loaded on start-up. This can be used, for instance, to enable OpenSSL in your application. Simply set the paths to the required libssl.so and libcrypto.so libraries here and OpenSSL should be enabled automatically."
)

define_property(TARGET
    PROPERTY
        QT_ANDROID_EXTRA_PLUGINS
    BRIEF_DOCS
        "This variable can be used to specify different resources that your project has to bundle but cannot be delivered through the assets system, such as qml plugins."
    FULL_DOCS
        "This variable can be used to specify different resources that your project has to bundle but cannot be delivered through the assets system, such as qml plugins. When using this variable, androiddeployqt will make sure everything is packaged and deployed properly."
)

define_property(TARGET
    PROPERTY
        QT_ANDROID_PACKAGE_SOURCE_DIR
    BRIEF_DOCS
        "This variable can be used to specify a directory where additions and modifications can be made to the default Android package template."
    FULL_DOCS
        "This variable can be used to specify a directory where additions and modifications can be made to the default Android package template. The androiddeployqt tool will copy the application template from Qt into the build directory, and then it will copy the contents of the ANDROID_PACKAGE_SOURCE_DIR on top of this, overwriting any existing files. The update step where parts of the source files are modified automatically to reflect your other settings is then run on the resulting merged package. If you, for instance, want to make a custom AndroidManifest.xml for your application, then place this directly into the folder specified in this variable. You can also add custom Java files in ANDROID_PACKAGE_SOURCE_DIR/src."
)

define_property(TARGET
    PROPERTY
        QT_ANDROID_APPLICATION_ARGUMENTS
    BRIEF_DOCS
        "This variable can be used to specify command-line arguments to the Android app."
    FULL_DOCS
        "Specifies extra command-line arguments to the Android app using the AndroidManifest.xml with the tag android.app.arguments."
)

define_property(TARGET
    PROPERTY
        QT_ANDROID_DEPLOYMENT_SETTINGS_FILE
    BRIEF_DOCS
        "This variable is used to specify the deployment settings JSON file for androiddeployqt."
    FULL_DOCS
        "This variable points to the path of the deployment settings JSON file, which holds properties required by androiddeployqt to package the Android app."
)

# Returns test execution arguments for Android targets
function(qt_internal_android_test_arguments target out_test_runner out_test_arguments)
    set(${out_test_runner} "${QT_HOST_PATH}/${QT${PROJECT_VERSION_MAJOR}_HOST_INFO_BINDIR}/androidtestrunner" PARENT_SCOPE)
    set(deployment_tool "${QT_HOST_PATH}/${QT${PROJECT_VERSION_MAJOR}_HOST_INFO_BINDIR}/androiddeployqt")

    get_target_property(deployment_file ${target} QT_ANDROID_DEPLOYMENT_SETTINGS_FILE)
    if (NOT deployment_file)
        message(FATAL_ERROR "Target ${target} is not a valid android executable target\n")
    endif()

    set(target_binary_dir "$<TARGET_PROPERTY:${target},BINARY_DIR>")
    set(apk_dir "${target_binary_dir}/android-build")

    set(${out_test_arguments}
        "--path" "${apk_dir}"
        "--adb" "${ANDROID_SDK_ROOT}/platform-tools/adb"
        "--skip-install-root"
        "--make" "${CMAKE_COMMAND} --build ${CMAKE_BINARY_DIR} --target ${target}_make_apk"
        "--apk" "${apk_dir}/${target}.apk"
        "--verbose"
        PARENT_SCOPE
    )
endfunction()
