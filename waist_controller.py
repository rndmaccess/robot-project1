from code.maestro import Controller

class WaistController:
    def __init__(self):
        pass

    def rotate(self, angle, chan):
        controller = Controller()
        # This range is a safe range between what angles the robot can turn
        controller.setRange(chan, 0, 180)
        controller.setSpeed(chan, 45)
        controller.setTarget(chan, angle)