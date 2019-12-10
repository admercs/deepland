cmake_minimum_required(VERSION 2.8.12)

if (POLICY CMP0048)
  cmake_policy(SET CMP0048 NEW)
endif (POLICY CMP0048)

project(deepland)

if (CMAKE_VERSION VERSION_LESS "3.1")
  add_definitions(-std=c++11)
else()
  set(CMAKE_CXX_STANDARD 11)
  set(CMAKE_CXX_STANDARD_REQUIRED ON)
  if(NOT CYGWIN)
    set(CMAKE_CXX_EXTENSIONS OFF)
  endif()
endif()

set(DEEPLAND_VERSION 0.5)

# Set source directory
set(SOURCE_DIR "src")

# Tell CMake that headers are also in SOURCE_DIR
include_directories("include")

# List source files
set(SOURCES "${SOURCE_DIR}/ops.cc")

# Set output directories to Python package location
#add_library(${PROJECT_NAME} STATIC ${SOURCES})
#set(LIBRARY_OUTPUT_DIRECTORY ${PROJECT_NAME})
#set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_NAME})
#set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_NAME})
#set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_NAME})

# pybind11
add_subdirectory("lib/pybind11")

pybind11_add_module("ops" SHARED ${SOURCES} "${SOURCE_DIR}/bindings_ops.cc")

# GoogleTest
enable_testing()

message(STATUS "Building tests for GoogleTest...")

set(TEST_NAME "${PROJECT_NAME}_test")

set(TEST_DIR "tests")

set(TEST_SOURCES
  "${TEST_DIR}/tests_main.cc"
  "${TEST_DIR}/ops_test.cc")

# Prevent overriding the parent project's compiler/linker
# settings on Windows
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

# Add googletest directly to our build. This defines
# the gtest and gtest_main targets.
add_subdirectory("lib/googletest" EXCLUDE_FROM_ALL)

# The gtest/gtest_main targets carry header search path
# dependencies automatically when using CMake 2.8.11 or
# later. Otherwise we have to add them here ourselves.
if (CMAKE_VERSION VERSION_LESS 2.8.11)
  include_directories("${gtest_SOURCE_DIR}/include")
endif()

# Now simply link against gtest or gtest_main as needed, e.g.,
add_executable(${TEST_NAME} ${TEST_SOURCES} ${SOURCES})
target_link_libraries(${TEST_NAME} gtest gtest_main)
add_test(NAME test1 COMMAND ${TEST_NAME})

message(STATUS "CMake script complete!")

