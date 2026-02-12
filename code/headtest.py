from robot import Robot

r = Robot()
speed = 8000

r.pan_head(6000)
i = input()


r.pan_head(speed)
print("Speed = " + str(i))

i = input()

r.pan_head(6000)
r.close()




