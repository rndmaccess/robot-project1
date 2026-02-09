from code.maestro import Controller

class WaistController:
    def __init__(self):
        pass

    def rotate(self, angle, servo):
        controller = Controller()
        angle = self._apply_limit(angle, 0, 180)

        pass

    def _apply_limit(self, angle, min_limit, max_limit):
        return max(min_limit, min(angle, max_limit))