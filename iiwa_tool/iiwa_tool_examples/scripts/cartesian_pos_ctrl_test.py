#!/usr/bin/env python

import time
from math import pi
import rospy

from iiwa_msgs.msg import CartesianPose
from geometry_msgs.msg import PoseStamped

curr_pos = 0

# class listener:
#     def __init__(self):
#         self.current_pos = None
#
#     def pose_cb(self, data):
#         self.current_pos = data


# def pose_subscriber(states):
#     pose_sub = rospy.Subscriber('/iiwa/state/CartesianPose', CartesianPose)#, states.pose_cb)
    # rospy.spin()

def pose_publisher():
    x_0 = PoseStamped()
    x_1 = PoseStamped()
    x_2 = PoseStamped()

    x0 = CartesianPose()
    x1 = CartesianPose()
    x2 = CartesianPose()

    x_0.pose.position.z = 1.3
    x_0.pose.orientation.w = 1.0

    x_1.pose.position.x = 0.2
    x_1.pose.position.z = 1.0
    x_1.pose.orientation.w = 1.0

    x_2.pose.position.x = -0.2
    x_2.pose.position.z = 1.0
    x_2.pose.orientation.w = 1.0

    rate = rospy.Rate(.25) # 0.25 Hz => 4 s

    # states = listener()
    # pose_subscriber(states)

    x0.poseStamped = x_0
    x1.poseStamped = x_1
    x2.poseStamped = x_2

    while not rospy.is_shutdown():
        rospy.loginfo("Publishing pos x_0: \n{}".format(x_0.pose))
        pose_pub.publish(x0)
        rate.sleep()

        rospy.loginfo("Publishing pos x_1: \n{}".format(x_1.pose.position))
        pose_pub.publish(x1)
        rate.sleep()
        #
        # rospy.loginfo("Publishing pos x_2: \n{}".format(x_2.pose.position))
        # pose_pub.publish(x_2)
        # rate.sleep()
        #
        # rospy.loginfo("Publishing pos x_1: \n{}".format(x_1.pose.position))
        # pose_pub.publish(x_1)
        # rate.sleep()
        # print("\n\n\n\n x_0: \n", x_0)
        # print("\n\n\n\n x_1: \n", x_1)
        # print("\n\n\n\n curr_pos: \n", states.current_pos)

if __name__ == "__main__":

    pose_pub = rospy.Publisher('/iiwa/command/CartesianPose', CartesianPose, queue_size = 10)
    rospy.init_node('cart_pos_ctrl', anonymous=True)

    try:
        pose_publisher()
    except KeyboardInterrupt:
        print("Stopping controller...")
