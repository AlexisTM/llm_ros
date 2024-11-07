cmake_minimum_required(VERSION 3.8)
project(llm_msgs)


if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(MSG_FILES
)
set(SRV_FILES
  srv/Prompt.srv
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${MSG_FILES}
  ${SRV_FILES}
  DEPENDENCIES builtin_interfaces
  ADD_LINTER_TESTS
)

ament_package()
