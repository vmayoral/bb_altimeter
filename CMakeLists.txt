cmake_minimum_required(VERSION 2.8.3)
project(bb_altimeter)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS rospy std_msgs)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES bb_sharp_IR
  CATKIN_DEPENDS rospy std_msgs
#  DEPENDS system_lib
)

include_directories(include
    ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS scripts/i2ctools_python.py scripts/mpl2115a2.py scripts/test-mpl2115a2.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

