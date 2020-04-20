#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def rotate(speed, angle):

     #Starts a new node
     rospy.init_node('robot_cleaner', anonymous=True)
     velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
     vel_msg = Twist()
 
     #Converting from angles to radians
     angular_speed = speed*2*PI/360
     relative_angle = angle*2*PI/360
  
     # Define sense of rotation
     vel_msg.angular.z = abs(angular_speed)
     # Setting the current time for distance calculus
     t0 = rospy.Time.now().to_sec()
     current_angle = 0
 
     while(current_angle < relative_angle):
         velocity_publisher.publish(vel_msg)
         t1 = rospy.Time.now().to_sec()
         current_angle = angular_speed*(t1-t0)
 
 
     #Forcing our robot to stop
     vel_msg.angular.z = 0
     velocity_publisher.publish(vel_msg)



def move(speed, distance):
     # Starts a new node
     rospy.init_node('robot_cleaner', anonymous=True)
     velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
     vel_msg = Twist()

     #Go forward
     vel_msg.linear.x = abs(speed)
 
     #Setting the current time for distance calculus
     t0 = rospy.Time.now().to_sec()
     current_distance = 0
 
     #Loop to move the turtle in an specified distance
     while(current_distance < distance):
         #Publish the velocity
         velocity_publisher.publish(vel_msg)
         #Takes actual time to velocity calculus
         t1=rospy.Time.now().to_sec()
         #Calculates distancePoseStamped
         current_distance= speed*(t1-t0)
     #After the loop, stops the robot
     vel_msg.linear.x = 0
     #Force the robot to stop
     velocity_publisher.publish(vel_msg)

def circle(speed, angle, x_linear):

     #Starts a new node
     rospy.init_node('robot_cleaner', anonymous=True)
     velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
     vel_msg = Twist()
 
     #Converting from angles to radians
     angular_speed = speed*2*PI/360
     relative_angle = angle*2*PI/360

     #Use of linear components on the x axis
     vel_msg.linear.x=x_linear
 
     # Define sense of rotation
     vel_msg.angular.z = abs(angular_speed)
     # Setting the current time for distance calculus
     t0 = rospy.Time.now().to_sec()
     current_angle = 0
 
     while(current_angle < relative_angle):
         velocity_publisher.publish(vel_msg)
         t1 = rospy.Time.now().to_sec()
         current_angle = angular_speed*(t1-t0)
 
 
     #Forcing our robot to stop
     vel_msg.angular.z = 0
     velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
     try:
	 move(1,4)
	 rotate(30,90)
	 print("do a circle")
	 circle(50,360,3.5)
	 print("do a square")
	 move(1,4)
	 rotate(30,90)
	 move(1,8)
	 rotate(30,90)
	 move(1,8)
	 rotate(30,90)
	 move(1,8)
	 rotate(30,90)
	 move(1,4)
     except rospy.ROSInterruptException:
         pass
