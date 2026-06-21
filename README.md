# Turtle Controller

ROS2 Python node that publishes velocities to the turtlesim node.

## Package

turtle_controller

## Node

circle_publisher

## Topic

/turtle1/cmd_vel

## Message Type

geometry_msgs/msg/Twist

## Behavior

The turtle takes a circular path by publishing the following:

* linear.x = 0.2
* angular.z = 0.5

## Build

colcon build --packages-select turtle_controller

## Run

ros2 run turtlesim turtlesim_node

ros2 run turtle_controller circle_publisher
