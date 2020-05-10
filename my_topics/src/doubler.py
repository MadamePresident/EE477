#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('doubler') 	# initialize node

def callback(msg): 	
	doubled = Int32() 				# declare
	doubled.data = msg.data * 2 	# double
	pub.publish(doubled) 			# publish in callback!

	sub = rospy.Subscriber('number', Int32, callback)
	pub = rospy.Publisher('doubled', Int32, queue-size = 3)

	rospy.spin() 	# keep node running until shut down