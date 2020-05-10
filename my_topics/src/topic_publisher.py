#!/usr/bin/env python
# ^shebang line
# Add packages as dependencies
import rospy
from std_msgs.msg import Int32 # standard int

# Setup: initialize node, register topic, set rate
rospy.init_node( # initialize node
  'topic_publisher' # node default name
)
pub = rospy.Publisher( # register topic w/roscore, creates object to assign to pub variable
  'counter', # topic name
  Int32, # topic type
  queue_size=5 # queue size
)
rate = rospy.Rate(2) # adaptive rate in Hz, set rate we like to rate variable

# Loop: publish, count, sleep
count = 0	# Set count at 0
while not rospy.is_shutdown(): # until ctrl-c
    pub.publish(count) # publish count
    count += 1 # increment
    rate.sleep() # set by rospy.Rate above, adaptively wait/ sleep diff lengths depending on execution time