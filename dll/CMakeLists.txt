include(CMakePackageConfigHeleprs)
include(GenerateExportHeader)

add_library(lib SHARED lib.cpp)
generate_export_header(lib)
target_include_directories(
    lib
    PUBLIC
    "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR};${CMAKE_CURRENT_BINARY_DIR}>"
)

install(
    TARGETS lib
    RUNTIME DESTINATION dll
)

