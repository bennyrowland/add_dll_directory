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
    ARCHIVE DESTINATION dll
)

find_package(PythonExtensions REQUIRED)

add_library(_sub MODULE sub/_sub.cpp)
target_link_libraries(_sub lib)
python_extension_module(_sub)
install(
    TARGETS _sub
    LIBRARY DESTINATION dll/sub
)

