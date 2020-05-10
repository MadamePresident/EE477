#!/usr/bin/env python
import rospy
from my_topics.msg import Complex # custom message type
from random import random # for random numbers!

rospy.init_node('message_publisher') #initialize node

pub = rospy.Publisher( # register topic
	'complex',		   # topic name
	Complex,		   # custom message type
	queue_size = 3	   # queue size
)

rate = rospy.Rate(2)	# set rate

while not rospy.is_shutdown(): # loop
	msg = Complex()				# declare type
	msg.real = random()			# assign value
	msg.imaginary = random()	# assign value

	pub.publish(msg)	# publish!
	rate.sleep()		# sleep to keep rate