execute_process(COMMAND "/home/yang/mdk-T/catkin_ws/build_isolated/miro2_msg/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/yang/mdk-T/catkin_ws/build_isolated/miro2_msg/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
