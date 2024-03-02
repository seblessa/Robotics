"""
IRI - TP1 - Ex 2
By: Gonçalo Leão
"""

from controller import Robot
from controllers.utils import cmd_vel

robot: Robot = Robot()

# v = r*w

v = 0.1
r = 0.125
w = v/r

cmd_vel(robot, v, w)
robot.step(50000)  # 1000 ms
