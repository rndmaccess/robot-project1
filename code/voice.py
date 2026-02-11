from espeakng import ESpeakNG

class Voice:

    espeak : ESpeakNG
    def __init__(self, espeak):
        self.espeak = espeak

    def say(self, message):
        self.espeak.say(message)
