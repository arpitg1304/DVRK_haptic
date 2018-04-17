cmake_minimum_required(VERSION 3.9)
project(DVRK_haptic)

set(CMAKE_CXX_STANDARD 11)

add_executable(DVRK_haptic
        08-bullet-coordination.cpp
        081-bullet-coordination.cpp
        euler2quat.py
        gripper.py
        gripper_R.py
        quat2eul.py
        README.md
        test2.py
        test_sony.py)
