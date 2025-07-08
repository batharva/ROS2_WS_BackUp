cmake_minimum_required(VERSION 3.8)
project(my_first_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)

add_executable(cpp_node src/my_first_node.cpp)
ament_target_dependencies(cpp_node rclcpp)

add_executable(robot_news_station src/my_first_publisher.cpp)
ament_target_dependencies(robot_news_station rclcpp example_interfaces)


add_executable(robot_news_subscriber src/my_first_subscriber.cpp)
ament_target_dependencies(robot_news_subscriber rclcpp example_interfaces)


add_executable(add_two_ints_server src/my_first_service.cpp)
ament_target_dependencies(add_two_ints_server rclcpp example_interfaces)


add_executable(add_two_ints_client src/my_first_client.cpp)
ament_target_dependencies(add_two_ints_client rclcpp example_interfaces)

install(TARGETS
  cpp_node
  robot_news_station
  robot_news_subscriber
  add_two_ints_server
  add_two_ints_client
  DESTINATION lib/${PROJECT_NAME}
)
ament_package()
