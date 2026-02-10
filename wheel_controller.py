from code.maestro import Controller

class WheelController:
    def __init__(self):
        pass

    def drive(self, speed, chan):
        controller = Controller()
        # This will be how fast the robot goes from point a to b.
        # We can tweak this if we need it to go faster!
        controller.setRange(chan, 0, 75)
        controller.setSpeed(chan, speed)