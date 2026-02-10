from head_controller import HeadController
from waist_controller import WaistController
from wheel_controller import WheelController


class Robot:
    def __init__(self):
        # Add the logic for tty1 vs tty0 here
        pass

    def pan_head(self, angle, chan):
        controller = HeadController()
        controller.pan(angle, chan)

    def tilt_head(self, angle, chan):
        controller = HeadController()
        controller.tilt(angle, chan)

    def rotate_waist(self, angle, chan):
        controller = WaistController()
        controller.rotate(angle, chan)

    def drive_wheels(self, robot_range, chan):
        controller = WheelController()
        controller.drive(robot_range, chan)
