# motor channels = 14 & 15

from robot import Robot
import time

r = Robot()
speed = 8000

r.rotate_waist(0)
i = input()
for i in range(6000, 8000):
    r.rotate_waist(i)
    print("Speed = " + str(i))

i = input()

r.rotate_waist(0)
r.close()

