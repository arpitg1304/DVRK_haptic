import rospy
import math
import tf
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Wrench
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Joy
import std_msgs.msg
from std_msgs.msg import Float64
from std_msgs.msg import String
import os
import pprint
import pygame
from geomagic_control.msg import DeviceFeedback

import sys, termios, tty, os, time
pub_f_gt = rospy.Publisher('/Geomagic/force_feedback', DeviceFeedback,  queue_size=1)



def callback(data):
    from geometry_msgs.msg import PoseStamped
    msg = PoseStamped()
    msg = data

    msg.pose.position.x = data.pose.position.x * -0.005
    msg.pose.position.y = data.pose.position.y * -0.005
    msg.pose.position.z = data.pose.position.z * 0.005

    pub_gt = rospy.Publisher('/dvrk/MTML/position_cartesian_current', PoseStamped, queue_size=1)
    #print(msg)
    #print('here')
    #rospy.init_node('MT_force', anonymous=True)
    pub_gt.publish(msg)
    #print(msg.pose.position.x)
    #print(msg.pose.position.y)

# def call_force(data):
#     print('in force')
#     force_GT = DeviceFeedback()
#     chai_force = data
#
#
#     # pub_f_gt = rospy.Publisher('/Geomagic/force_feedback', DeviceFeedback,  queue_size=1)
#     f_x = data.force.x
#     f_y = data.force.y
#     f_z = data.force.z
#
#     if (abs(f_x) < 2 and abs(f_y)<2 and abs(f_z)<2):
#         force_GT.force.x = f_x
#         force_GT.force.y = f_y
#         force_GT.force.z = f_z
#         pub_f_gt.publish(force_GT)

def main():
    from geometry_msgs.msg import PoseStamped
    rospy.init_node('GT_talker', anonymous=True)
    sub_MTML = rospy.Subscriber('/Geomagic/pose', PoseStamped, callback)

    #sub_MTML_force = rospy.Subscriber('/dvrk/MTML/set_wrench_body', PoseStamped, call_force)

    # sub_MTML = rospy.Subscriber('/Geomagic/pose', PoseStamped, callback)
    rospy.spin()


if __name__ == '__main__':
    main()