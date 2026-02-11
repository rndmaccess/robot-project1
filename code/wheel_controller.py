from maestro import Controller
# Wheel Channels = 14 & 15

__MOTOR_MIN = 1200 
__MOTOR_MAX = 1800
class WheelController:
    controller : Controller 
    def __init__(self, controller : Controller):
        self.controller = controller
        pass

    def drive(self, speed, chan):

        # This will be how fast the robot goes from point a to b.
        # We can tweak this if we need it to go faster!
        # 1200 min 1800 max

        self.controller.setRange(chan, __MOTOR_MIN, __MOTOR_MAX)

        self.controller.setSpeed(chan, speed)
        self.controller.setTarget(chan,speed)
	
	
