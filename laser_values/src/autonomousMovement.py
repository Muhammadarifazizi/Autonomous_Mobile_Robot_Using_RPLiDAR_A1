#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from laser_values import callback
from motor_movement import forward, backward, left, right, obliqueLeftBackward, obliqueLeftForward, obliqueRigthBackward, obliqueRigthForward


def autonomous():
    if callback > 0.20:
        forward

rospy.init_node('autonomous')
sub = rospy.Subscriber('/scan', LaserScan, )