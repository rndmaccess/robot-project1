# motor channels = 14 & 15

from robot import Robot
import time

r = Robot()


r.drive_wheels(1200)

time.sleep(1.0)

r.drive_wheels(1800)

time.sleep(1.0)

r.drive_wheels(1200)


