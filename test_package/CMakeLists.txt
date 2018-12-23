project(test_package)
cmake_minimum_required(VERSION 2.8.11)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME} test_package.cpp)

if(USE_FIND_PACKAGE)
find_package(spdlog CONFIG REQUIRED)
find_package(fmt CONFIG REQUIRED)

target_link_libraries(${PROJECT_NAME} spdlog::spdlog fmt::fmt)

else(USE_FIND_PACKAGE)

target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

endif(USE_FIND_PACKAGE)

set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 11)
