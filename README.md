# Kratos ROS2 Week 1. TurtleBot Circle Controller

## Overview

I worked on a project that makes a TurtleBot move in a circle. I used ROS2 and Python to create a node that sends speed commands to the robot.

The node keeps sending `geometry_msgs/msg/Twist` messages to the `/cmd_vel` topic. This makes the robot move in a circle.

## Package

`turtle_controller`

## Node

`circle_publisher`

## Topic

`/cmd_vel`

## Message Type

`geometry_msgs/msg/Twist`

## System Requirements

* You need Ubuntu 22.04 on your computer.

* You need ROS2 Humble installed.

* You need Python 3.

* You need the Genesis Simulator.

## Build Instructions

To get the package do this:

```bash

cd ~/ros2_ws/src

git clone https://github.com/Quxdros/kratos-ros2-week1.git

```

build the workspace:

```bash

cd ~/ros2_ws

colcon build

source install/setup.bash

```

## Running the Simulation

### Terminal 1

Open a terminal and run the Genesis TurtleBot simulation:

```bash

python3 turtlebot_sim.py

```

### Terminal 2

In another terminal source ROS2 and run the controller node:

```bash

source /opt/ros//setup.bash

source ~/ros2_ws/install/setup.bash

ros2 run turtle_controller circle_publisher

```

## Verification

To check if the node is sending speed commands:

```bash

ros2 topic echo /cmd_vel

```

You should see something like this:

```text

linear:

x: 0.2

angular:

z: 0.5

```

## Demonstrated ROS2 Concepts

* I used ROS2 Nodes to control the TurtleBot.

* I used ROS2 Topics to send messages.

* I used Publishers to send speed commands.

* I used `geometry_msgs/msg/Twist` messages.

* I created a Python-based ROS2 package.

* I integrated the Genesis Simulator.

## Expected Result

The TurtleBot should keep moving in a circle, inside the Genesis simulation.
