from code.maestro import Controller

class WheelController:
    def __init__(self):
        pass

    def drive(self, robot_range, servo):
        controller = Controller()
        # This will be how fast the robot goes from point a to b.
        # We can tweak this if we need it to go faster!
        robot_range = self._apply_limit(robot_range, 0, 75)
        pass

    def _apply_limit(self, robot_range, min_limit, max_limit):
        return max(min_limit, min(robot_range, max_limit))