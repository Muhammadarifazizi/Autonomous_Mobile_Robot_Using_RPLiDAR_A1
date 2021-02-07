#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
import statistics

minDistance = 0.20
maxDistance = 6

#distance oblique right
def obliqueRight(msg):
    distanceList = []
    for i in range(20, 60):
        #median from 20 - 60 deg
        if msg.ranges[i] > minDistance and msg.ranges[i]< maxDistance:
            '''
            show distance for each degree
            newdistance = str(i)+':'+str(msg.ranges[i])
            distanceList.append(newdistance)
            '''
            distanceList.append(msg.ranges[i]) 
        else:
            '''because RPLiDAR A1 have some problem when reading distace less than 12 cm or more than 6 meter
            lidar will display infinite distance, so to minimize this problem, we use default distance for each case 
            '''
            distanceList.append(0.12)
            
    medianDistance = statistics.median(distanceList)
    #print(medianDistance)
    return medianDistance

def obliqueLeft(msg):
    distanceList = []
    for i in range(300, 340):
        if msg.ranges[i]>minDistance and msg.ranges[i]<maxDistance:
            distanceList.append(msg.ranges[i])
        else:
            distanceList.append(0.12) 
        
    medianDistance = statistics.median(distanceList)
    #print(medianDistance)
    return medianDistance

#get median distance for front
def front(msg):
    distanceList =[]
    #get all distance frontleft
    for i in range(340, 360):
        if msg.ranges[i]>minDistance and msg.ranges[i]<maxDistance:
            distanceList.append(msg.ranges[i])
        else:
            distanceList.append(0.12)
    #get all distance frontright
    for i in range(0, 20):
        if msg.ranges[i]>minDistance and msg.ranges[i]<maxDistance:
            distanceList.append(msg.ranges[i])
        else:
            distanceList.append(0.12) 
    #print(distanceList)
    medianDistance = statistics.median(distanceList)
    #print(medianDistance)
    return medianDistance

#collect all median distance from front, obliqueRight, and obliqueLeft 
def allDistance(msg):
    dictDistance={}
    #listDistance = []
    dictDistance['front'] = front(msg)
    dictDistance['obliqueLeft'] = obliqueLeft(msg)
    dictDistance['obliqueRight'] = obliqueRight(msg) 
    #listDistance.append(dictDistance)
    print(dictDistance)

rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, allDistance)
rospy.spin()

