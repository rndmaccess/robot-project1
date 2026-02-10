import maestro

import time

port = 3

servo = maestro.Controller()

print("Init Servo " + str(port))

servo.setTarget(port,0)

time.sleep(1)

print("Moving Servo " + str(port))

servo.setTarget(port,6000)


time.sleep(1)

print("Returning Servo " + str(port) + " to default position")

servo.setTarget(port,0)


servo.close()