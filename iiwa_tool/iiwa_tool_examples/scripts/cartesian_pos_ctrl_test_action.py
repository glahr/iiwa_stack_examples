#!/usr/bin/env python

import time
from math import pi
import rospy

from iiwa_msgs.msg import CartesianPose, MoveToCartesianPoseGoal, MoveToCartesianPoseAction
from geometry_msgs.msg import PoseStamped
import actionlib

def cart_action():
    robot = actionlib.SimpleActionClient('/iiwa/action/move_to_cartesian_pose', MoveToCartesianPoseAction)

    print("waiting for server")
    robot.wait_for_server()

    try:
        cart_pos_goal_0 = MoveToCartesianPoseGoal()
        cart_pos_goal_1 = MoveToCartesianPoseGoal()
        cart_pos_goal_2 = MoveToCartesianPoseGoal()

        cart_pos_goal_0.cartesian_pose.poseStamped.pose.position.z = 1.3
        cart_pos_goal_0.cartesian_pose.poseStamped.pose.orientation.w = 1

        cart_pos_goal_1.cartesian_pose.poseStamped.pose.position.x = 0.2
        cart_pos_goal_1.cartesian_pose.poseStamped.pose.position.z = 1.0
        cart_pos_goal_1.cartesian_pose.poseStamped.pose.orientation.w = 1

        cart_pos_goal_2.cartesian_pose.poseStamped.pose.position.x = -0.2
        cart_pos_goal_2.cartesian_pose.poseStamped.pose.position.z = 1.0
        cart_pos_goal_2.cartesian_pose.poseStamped.pose.orientation.w = 1

        while not rospy.is_shutdown():

            print("sending goal 0")
            robot.send_goal(cart_pos_goal_0)

            robot.wait_for_result()
            print("Goal achieved")

            print("sending goal 1")
            robot.send_goal(cart_pos_goal_1)
            robot.wait_for_result()
            print("Goal achieved")

            print("sending goal 2")
            robot.send_goal(cart_pos_goal_2)
            robot.wait_for_result()
            print("Goal achieved")

            rate = rospy.Rate(1) # 1 Hz => 1 s
    except KeyboardInterrupt:
        robot.cancel_goal()
        print("control stopped")



if __name__ == "__main__":

    # pose_pub = rospy.Publisher('/iiwa/command/CartesianPose', PoseStamped, queue_size = 10)
    rospy.init_node('cart_pos_ctrl_client', anonymous=True)

    try:
        cart_action()
    except KeyboardInterrupt:
        print("Stopping controller...")
