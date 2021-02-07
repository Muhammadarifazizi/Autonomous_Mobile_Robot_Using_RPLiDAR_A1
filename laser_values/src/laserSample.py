#!/usr/bin/env python3
import ros
import rospy
from sensor_msgs.msg import LaserScan

def RadToDeg(x):
    return ((x*180)/3.14)

def ScanCallBack(msg):
    count = msg.scan_time / msg.time_increment
    print("Laser scan",str(msg.header.frame_id, ":",float(count)))

#ScanCallBack()