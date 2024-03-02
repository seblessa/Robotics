"""
IRI - TP1 - Ex 4
By: Gonçalo Leão
"""

from controller import Robot
from controllers.utils import cmd_vel, move_forward

robot: Robot = Robot()

# v = d/t

# velocity in m/s
v = 0.1

# tile length in meters
d = 0.125

# t = d/v
# time to travel 2 tiles at 0.1 m/s in milliseconds
t = int(((2*d)/v)*1000)

# move forward 2 tiles at 0.1 m/s
cmd_vel(robot, v, 0)
robot.step(t)

# stop for 1 second
cmd_vel(robot, 0, 0)
robot.step(1000)

# move backwards 2 tiles at 0.1 m/s
cmd_vel(robot, -v, 0)
robot.step(t)

