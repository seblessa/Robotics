"""
IRI - TP1 - Ex 7
By: Gonçalo Leão
"""
import math

from controller import Robot
from controllers.utils import cmd_vel

robot: Robot = Robot()

w = -math.pi

v = 0

while True:
    cmd_vel(robot, v, w)
    robot.step(1)
    if v < 2:
        v += 0.0001
