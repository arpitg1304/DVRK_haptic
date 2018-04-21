import rospy
import math
import tf
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Joy
import std_msgs.msg
from std_msgs.msg import Float64
from std_msgs.msg import String

import os
import pprint
import pygame

import sys, termios, tty, os, time

global r
r = .05

def angleUpdate(q, a, op):
    #print q
    euler = tf.transformations.euler_from_quaternion(q)
    roll = euler[0]
    pitch = euler[1]
    yaw = euler[2]

    eu = [roll, pitch, yaw]
    eu[a] = eu[a] + r * op
    print(eu)
    q_new = tf.transformations.quaternion_from_euler(eu[0], eu[1], eu[2])
    return q_new

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

from geometry_msgs.msg import PoseStamped

def callback(data):
    print('pressed l')
    print(data)

def getSlavePos():

    slave_pos = PoseStamped()
    #rospy.init_node('listener', anonymous=True)
    slave_subs = rospy.Subscriber('/dvrk/MTMR/position_cartesian_current', PoseStamped, callback)
    rospy.loginfo(slave_subs)
    #rospy.spin()
    rospy.sleep(0.5)

def pose():

    msg_grip = JointState()
    pub3 = rospy.Publisher('/dvrk/MTML/state_gripper_current', JointState, queue_size=1)
    msg_grip.header.frame_id = "map"
    msg_grip.position = [0]
    msg_grip.position[0] = -0.10

    im = 0;
    pub2 = rospy.Publisher('/dvrk/MTML/position_cartesian_current', PoseStamped, queue_size=1)
    rospy.init_node('poser', anonymous=True)

    msg = PoseStamped()
    rate = rospy.Rate(10)

    msg.header.frame_id = "map"
    msg.header.stamp = rospy.get_rostime()

    msg.pose.position.x = 0.20
    msg.pose.position.y = 0.10
    msg.pose.position.z = -0.25

    msg.pose.orientation.x = 0.70
    msg.pose.orientation.y = 0.70
    msg.pose.orientation.z = 0.70
    msg.pose.orientation.w = 0

    msg_cam = Joy()

    while not rospy.is_shutdown():

        pub_cam = rospy.Publisher('/dvrk/footpedals/coag', Joy, queue_size=1)

        pub = rospy.Publisher('/dvrk/MTML/status', String, queue_size=1)
        hello_str = "This"
        pub.publish(hello_str)

        msg.pose.position.x = msg.pose.position.x
        msg.pose.position.y = msg.pose.position.y
        msg.pose.position.z = msg.pose.position.z

        msg.pose.orientation.x = msg.pose.orientation.x
        msg.pose.orientation.y = msg.pose.orientation.y
        msg.pose.orientation.z = msg.pose.orientation.z
        msg.pose.orientation.w = msg.pose.orientation.w

        char = getch()

        if (char == "c"):
            msg_cam.buttons = [1]
            pub_cam.publish(msg_cam)

        if (char == "v"):
            msg_cam.buttons = [0]
            pub_cam.publish(msg_cam)

        if (char == "n"):
            msg_grip.position[0] = msg_grip.position[0] + 0.1
            pub3.publish(msg_grip)

        if (char == "m"):
            msg_grip.position[0] = msg_grip.position[0] - 0.1
            pub3.publish(msg_grip)

        if (char == "p"):
            print("Stop!")
            exit(0)

        if char == "a":
            msg.pose.position.x = msg.pose.position.x - 0.01
            pub2.publish(msg)

            rate.sleep()
            print("Left pressed")
            

        elif char == "e":
            msg.pose.position.y = msg.pose.position.y + 0.01
            pub2.publish(msg)

            rate.sleep()
            print("Right pressed")
            

        elif char == "d":
            msg.pose.position.y = msg.pose.position.y - 0.01
            pub2.publish(msg)

            rate.sleep()
            print("Right pressed")
            

        elif char == "f":
            msg.pose.position.z = msg.pose.position.z + 0.01
            pub2.publish(msg)

            rate.sleep()
            print("Right pressed")
            

        elif char == "r":
            msg.pose.position.z = msg.pose.position.z - 0.01
            pub2.publish(msg)

            rate.sleep()
            print("Right pressed")
            

        elif char == "w":
            msg.pose.position.x = msg.pose.position.x + 0.01
            pub2.publish(msg)

            rate.sleep()
            print("Up pressed")

        elif char == "l":
            getSlavePos()


        elif char == "1":
            q = [msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w]
            q_new = angleUpdate(q, 0, 1)
            msg.pose.orientation.x = q_new[0]
            msg.pose.orientation.y = q_new[1]
            msg.pose.orientation.z = q_new[2]
            msg.pose.orientation.w = q_new[3]
            pub2.publish(msg)
            rate.sleep()
            

        elif char == "2":
            q = [msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w]
            q_new = angleUpdate(q, 0, -1)
            msg.pose.orientation.x = q_new[0]
            msg.pose.orientation.y = q_new[1]
            msg.pose.orientation.z = q_new[2]
            msg.pose.orientation.w = q_new[3]
            pub2.publish(msg)
            rate.sleep()

        elif char == "3":
            q = [msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w]
            q_new = angleUpdate(q, 1, 1)
            msg.pose.orientation.x = q_new[0]
            msg.pose.orientation.y = q_new[1]
            msg.pose.orientation.z = q_new[2]
            msg.pose.orientation.w = q_new[3]
            pub2.publish(msg)
            rate.sleep()

        elif char == "4":
            q = [msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w]
            q_new = angleUpdate(q, 1, -1)
            msg.pose.orientation.x = q_new[0]
            msg.pose.orientation.y = q_new[1]
            msg.pose.orientation.z = q_new[2]
            msg.pose.orientation.w = q_new[3]
            pub2.publish(msg)
            rate.sleep()

        elif char == "5":
            q = [msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w]
            q_new = angleUpdate(q, 2, 1)
            msg.pose.orientation.x = q_new[0]
            msg.pose.orientation.y = q_new[1]
            msg.pose.orientation.z = q_new[2]
            msg.pose.orientation.w = q_new[3]
            pub2.publish(msg)
            rate.sleep()

        elif char == "6":
            q = [msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w]
            q_new = angleUpdate(q, 2, -1)
            msg.pose.orientation.x = q_new[0]
            msg.pose.orientation.y = q_new[1]
            msg.pose.orientation.z = q_new[2]
            msg.pose.orientation.w = q_new[3]
            pub2.publish(msg)
            rate.sleep()

def talker():
    pub = rospy.Publisher('/dvrk/MTML/status', String, queue_size=1)

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(100) # 10hz
    hello_str = "This"
    rospy.loginfo(hello_str)
    while not rospy.is_shutdown():
        pub.publish(hello_str)

if __name__ == '__main__':
        pose()
