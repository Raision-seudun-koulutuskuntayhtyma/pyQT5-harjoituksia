# MODULE FOR CREATING BEEP SOUNDS

# Imported libraries and modules

import winsound

# Classes and functions

# Beep sounder
def create_sound(frequency, duration):
    winsound.Beep(frequency, duration * 1000)
