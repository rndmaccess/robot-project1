from head_controller import HeadController
from waist_controller import WaistController
from wheel_controller import WheelController
from voice import Voice
from espeakng import ESpeakNG
import maestro
class Robot:
    master_controller : maestro.Controller
    espeak : ESpeakNG
    head : HeadController
    wheels : WheelController
    waist : WaistController
    voice : Voice

    def __init__(self):
        # Add the logic for tty1 vs tty0 here
        self.master_controller = maestro.Controller()
        self.espeak = ESpeakNG()

        self.head = HeadController(self.master_controller)
        self.wheels = WheelController(self.master_controller)
        self.waist = WaistController(self.master_controller)
        self.voice = Voice(self.espeak)
        pass
    def close(self):
        self.master_controller.close()


    def pan_head(self, angle, chan):
        self.head.pan(angle, chan)

    def tilt_head(self, angle, chan):
        self.head.tilt(angle, chan)

    def rotate_waist(self, angle, chan):
        self.waist.rotate(angle, chan)

    def speak(self, message):
        self.voice.say(message)

    def drive_wheels(self, speed):
        self.wheels.drive(speed, 14)
