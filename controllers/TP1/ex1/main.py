"""
IRI - TP1 - Ex 1
By: Gonçalo Leão
"""

from controller import Robot
from controllers.utils import cmd_vel

# Create the Robot instance.
robot: Robot = Robot()

cmd_vel(robot, 0.1, 0)
robot.step(1000)  # 1000 ms
