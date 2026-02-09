from code.maestro import Controller

class HeadController:
    def __init__(self):
        pass

    def tilt(self, angle, servo):
        controller = Controller()
        # We can tweak these if we need more rotation!
        angle = self._apply_limit(angle, 45, 90)
        pass

    def pan(self, angle, servo):
        controller = Controller()
        # We can tweak these if we need more rotation!
        angle = self._apply_limit(angle, 0, 180)
        pass

    def _apply_limit(self, angle, min_limit, max_limit):
        return max(min_limit, min(angle, max_limit))