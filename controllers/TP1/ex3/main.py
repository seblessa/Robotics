"""
IRI - TP1 - Ex 3
By: Gonçalo Leão
"""

import math
from controller import Robot
from controllers.utils import cmd_vel

robot: Robot = Robot()

# v = r*w

# move forward 1 second
cmd_vel(robot, 0.1, 0)
robot.step(1000)  # 1000 ms

# stop for 1 second
cmd_vel(robot, 0, 0)
robot.step(1000)  # 1000 ms

# rotate itself clockwise endlessly for 180 degrees per second
# 180 degrees = pi radians
while True:
    cmd_vel(robot, 0, -math.pi)
    robot.step(1)

