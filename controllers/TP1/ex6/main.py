"""
IRI - TP1 - Ex 6
By: Gonçalo Leão
"""

from controller import Robot
from controllers.utils import cmd_vel

# gives an error but still works

robot: Robot = Robot()

v = 0.1
w = 0

w_limit = 1

while True:
    cmd_vel(robot, v, w)
    robot.step(1)
    if w < w_limit:
        w -= 0.01
