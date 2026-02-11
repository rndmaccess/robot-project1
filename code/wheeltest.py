# motor channels = 14 & 15

from robot import Robot
import time

r = Robot()
speed = 4000

r.drive_wheels(6000)
i = input()

r.drive_wheels(speed)
print("Speed = " + str(speed))

i = input()

r.drive_wheels(6000)
r.close()

