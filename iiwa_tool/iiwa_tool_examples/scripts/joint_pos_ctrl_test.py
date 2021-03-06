#!/usr/bin/env python

import time
from math import pi
import rospy

from iiwa_msgs.msg import JointPosition

# def joint_cb(data):
#     print(data)
#     print(type(data))
#     print("\n\n\n")

def joint_subscriber():
    pose_sub = rospy.Subscriber('/iiwa/state/JointPosition', JointPosition)#, joint_cb)
    # rospy.spin()

def joint_pos_pub():
    q_0 = JointPosition()
    q_1 = JointPosition()

    q_1.position.a1 = 30*pi/180
    q_1.position.a4 = 60*pi/180

    rate = rospy.Rate(0.25) # 0.25 Hz => 4 s

    while not rospy.is_shutdown():
        rospy.loginfo("Publishing pos q_0: \n{}".format(q_0.position))
        joint_pub.publish(q_0)
        rate.sleep()

        rospy.loginfo("Publishing pos q_1: \n{}".format(q_1.position))
        joint_pub.publish(q_1)
        rate.sleep()

if __name__ == "__main__":

    joint_pub = rospy.Publisher('/iiwa/command/JointPosition', JointPosition, queue_size = 10)
    rospy.init_node('joint_pos_ctrl', anonymous=True)

    try:
        joint_subscriber()
        joint_pos_pub()
    except KeyboardInterrupt:
        print("Stopping controller...")
