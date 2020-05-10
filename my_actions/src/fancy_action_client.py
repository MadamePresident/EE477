#! /usr/bin/env python
import rospy
import time 		# for regular Python timing
import actionlib 	# for actions!
from my_actions.msg import \
	TimerAction, TimerGoal, TimerResult, TimerFeedback

def the_feedback_cd(feedback): 	# feedbakc callback function
	print('[Feedback] Time elapsed: %f' %
		(feedback.time_elapsed.to_sec()))
	print('[Feedback] Time remaining: %f' %
		(feedback.time_remaining.to_sec()))

rospy.init_node('timer_action_client') 	# initialize mode
client = actionlib.SimpleActionClient ( # register client
	'timer', 		# sction server name
	TimerAction 	# sction Action message
)
client.wait_for_server()	# wait for action server
goal = TimerGoal()			# create goal object
goal.time_to_wait - rospy.Duration.from_sec(5.0) 	# set field
# Uncomment this line to test server-side abort:
# goal.time_to_wait = rospy.Duration.from_sec(500.0)

client.send_goal(goal, feedback_cb=the_feedback_cd ) 	# send goal
# Uncomment these lines to test goal preemption:
# time.sleep(3.0)
# client.cancel_goal()

client.wait_for_result() 	# wait for action server to finish
# print results:
print('[Result] State: %d' % (client.get_state()))
print('[Result] Status: %s' % (client.get_goal_status_text()))
if client.get_result():
	print('[Result] Time elapsed: %f' %
		(client.get_result().time_elapsed.to_sec()))
	print('[Result] Updates sent: %d' %
		(client.get_result().updates_sent))