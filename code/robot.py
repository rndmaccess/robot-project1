from head_controller import HeadController
from waist_controller import WaistController
from wheel_controller import WheelController
import maestro
class Robot:
    master_controller : maestro.Controller
    head : HeadController
    wheels : WheelController
    waist : WaistController

    def __init__(self):
        # Add the logic for tty1 vs tty0 here
        self.master_controller = maestro.Controller()

        self.head = HeadController(self.master_controller)
        self.wheels = WheelController(self.master_controller)
        self.waist = WaistController(self.master_controller)
        pass
    def close(self):
        self.master_controller.close()


    def pan_head(self, angle, chan):
        self.head.pan(angle, chan)

    def tilt_head(self, angle, chan):
        self.head.tilt(angle, chan)

    def rotate_waist(self, angle):
        self.waist.rotate(angle, 5)

    def drive_wheels(self, speed):
        self.wheels.drive(speed, 1)
