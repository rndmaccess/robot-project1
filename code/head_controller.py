from maestro import Controller

class HeadController:
    controller : Controller

    def __init__(self, controller : Controller):
        self.controller = controller 
        pass

    def tilt(self, angle, chan):
        # We can tweak these if we need more rotation!
        self.controller.setRange(chan, 0, 0)
        self.controller.setSpeed(chan, 0)
        self.controller.setAccel(chan, 0)
        self.controller.setTarget(chan, angle)

    def pan(self, angle, chan):
        # We can tweak these if we need more rotation!

        self.controller.setRange(chan, 0, 0)
        self.controller.setSpeed(chan, 0)
        self.controller.setAccel(chan, 0)
        self.controller.setTarget(chan, angle)
