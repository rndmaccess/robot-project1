from code.maestro import Controller

class HeadController:
    def __init__(self):
        pass

    def tilt(self, angle, chan):
        controller = Controller()
        # We can tweak these if we need more rotation!
        controller.setRange(chan, 45, 90)
        controller.setSpeed(chan, 45)
        controller.setTarget(chan, angle)

    def pan(self, angle, chan):
        controller = Controller()
        # We can tweak these if we need more rotation!
        controller.setRange(chan, 0, 180)
        controller.setSpeed(chan, 45)
        controller.setTarget(chan, angle)