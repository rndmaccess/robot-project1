from espeakng import ESpeakNG
import os

class Voice:

    espeak : ESpeakNG
    def __init__(self, espeak):
        self.espeak = espeak

    def say(self, message):
        os.system(f'espeak-ng "{message}"')
