"""
IRI - TP1 - Ex 5
By: Gonçalo Leão
"""

import math
from controller import Robot
from controllers.utils import move_forward, rotate

robot: Robot = Robot()


# tile length in meters
d = 0.125

while True:
    move_forward(robot,d*2, 0.1)
    rotate(robot, math.pi/2, 0.5)

