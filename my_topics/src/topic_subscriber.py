#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(msg):	# Callback for receiving messages
	print(msg.data)	# Print to terminal

rospy.init_node('topic_subscriber')	# Initialize node

sub = rospy.Subscriber('counter', Int32, callback)	# Subscribe

rospy.spin()	# Wait for node to be shut down