# Install script for directory: /home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/miro/miro-e_yufeng/mdk-T/catkin_ws/build/miro2_msg/catkin_generated/safe_execute_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/miro2_msg/msg" TYPE FILE FILES
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/adjust.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/affect_adjust.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/affect.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/animal_adjust.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/animal_state.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/funnel_web.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/img_annotation.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/object_ball.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/object_face.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/objects.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/object_tag.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/priority_peak.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/push.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/sensors_package.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/sleep_adjust.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/sleep.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/voice_state.msg"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/msg/BatteryState.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/miro2_msg/cmake" TYPE FILE FILES "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/build/miro2_msg/catkin_generated/installspace/miro2_msg-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/devel/include/miro2_msg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/devel/share/roseus/ros/miro2_msg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/devel/share/common-lisp/ros/miro2_msg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/devel/share/gennodejs/ros/miro2_msg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/devel/lib/python3/dist-packages/miro2_msg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/devel/lib/python3/dist-packages/miro2_msg" REGEX "/\\_\\_init\\_\\_\\.py$" EXCLUDE REGEX "/\\_\\_init\\_\\_\\.pyc$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/devel/lib/python3/dist-packages/miro2_msg" FILES_MATCHING REGEX "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/devel/lib/python3/dist-packages/miro2_msg/.+/__init__.pyc?$")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/build/miro2_msg/catkin_generated/installspace/miro2_msg.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/miro2_msg/cmake" TYPE FILE FILES "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/build/miro2_msg/catkin_generated/installspace/miro2_msg-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/miro2_msg/cmake" TYPE FILE FILES
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/build/miro2_msg/catkin_generated/installspace/miro2_msgConfig.cmake"
    "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/build/miro2_msg/catkin_generated/installspace/miro2_msgConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/miro2_msg" TYPE FILE FILES "/home/miro/miro-e_yufeng/mdk-T/catkin_ws/src/miro2_msg/package.xml")
endif()

