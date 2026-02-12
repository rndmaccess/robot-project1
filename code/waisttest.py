# motor channels = 14 & 15

from robot import Robot
import time

r = Robot()
speed = 8000

r.rotate_waist(6000)
i = input()


r.rotate_waist(speed)
print("Speed = " + str(i))

i = input()

r.rotate_waist(6000)
r.close()

