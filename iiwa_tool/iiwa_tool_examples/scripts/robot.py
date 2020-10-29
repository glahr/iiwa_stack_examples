#!/usr/bin/env python

import rospy
import actionlib

from iiwa_msgs.msg import CartesianPose, MoveToCartesianPoseGoal, MoveToCartesianPoseAction
from geometry_msgs.msg import PoseStamped

class Robot:

    def __init__(self):
        self.node_init()
        self.action_client = self.init_action_client()

    def init_action_client(self):
        client = actionlib.SimpleActionClient('/iiwa/action/move_to_cartesian_pose', MoveToCartesianPoseAction)
        rospy.loginfo("------- Waiting for server -------")
        client.wait_for_server()
        rospy.loginfo("------- Connected to server! -------")
        #self.stop_goals_admittance(client_admittance)
        #print("admittance = " + str(isinstance(client_admittance, unicode)))
        return client

    def node_init(self):
        rospy.init_node('iiwa_controller_experiments', anonymous=True)

    def done_cb(self, d1, d2):
        # print(d1)
        # print(d2)
        # print("\n")
        return

    def active_cb(self):
        # print(data)
        return

    def feedback_cb(self):
        return

    def move(self, x_lin = 0, y_lin = 0, z_lin = 0, x_ori = 0, y_ori = 0, z_ori = 0, w_ori = 0):

        goal = MoveToCartesianPoseGoal()
        goal.cartesian_pose.poseStamped.pose.position.x = x_lin
        goal.cartesian_pose.poseStamped.pose.position.y = y_lin
        goal.cartesian_pose.poseStamped.pose.position.z = z_lin
        goal.cartesian_pose.poseStamped.pose.orientation.x = x_ori
        goal.cartesian_pose.poseStamped.pose.orientation.y = y_ori
        goal.cartesian_pose.poseStamped.pose.orientation.z = z_ori
        goal.cartesian_pose.poseStamped.pose.orientation.w = w_ori

        self.action_client.send_goal(goal, self.done_cb, self.active_cb, self.feedback_cb)
        self.action_client.wait_for_result()
        # rospy.loginfo("Action done!")
