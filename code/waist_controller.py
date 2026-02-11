from maestro import Controller

class WaistController:

    controller : Controller
    def __init__(self, controller : Controller):
        self.controller = controller
        pass

    def rotate(self, angle, chan):
        # This range is a safe range between what angles the robot can turn
        self.controller.setRange(chan, 0, 0) 
        self.controller.setSpeed(chan, 0)
        self.controller.setAccel(chan,0)
        self.controller.setTarget(chan, angle)
