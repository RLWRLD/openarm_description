cmake_minimum_required(VERSION 3.10)
project(inspire_hand_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY RH56F1
  DESTINATION share/${PROJECT_NAME})

install(FILES LICENSE
  README.md
  DESTINATION share/${PROJECT_NAME})

ament_package()
