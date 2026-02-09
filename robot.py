from head_controller import HeadController
from waist_controller import WaistController
from wheel_controller import WheelController


class Robot:
    def __init__(self):
        # Add the logic for tty1 vs tty0 here
        pass

    def pan_head(self, angle, servo):
        controller = HeadController()
        controller.pan(angle, servo)

    def tilt_head(self, angle, servo):
        controller = HeadController()
        controller.tilt(angle, servo)

    def rotate_waist(self, angle, servo):
        controller = WaistController()
        controller.rotate(angle, servo)

    def drive_wheels(self, robot_range, servo):
        controller = WheelController()
        controller.drive(robot_range, servo)
