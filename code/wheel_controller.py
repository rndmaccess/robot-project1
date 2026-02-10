from maestro import Controller

class WheelController:
    controller : Controller 
    def __init__(self, controller : Controller):
        self.controller = controller
        pass

    def drive(self, speed, chan):
        # This will be how fast the robot goes from point a to b.
        # We can tweak this if we need it to go faster!
        self.controller.setRange(chan, 0, 75)
        self.controller.setSpeed(chan, speed)
