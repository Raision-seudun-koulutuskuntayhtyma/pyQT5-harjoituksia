# MODULE FOR CREATING BEEP SOUNDS

# Imported libraries and modules

import winsound

# Classes and functions

# Beep sounder
def create_sound(frequency, duration):
    """Sounds a beep tone

    Args:
        frequency (int): frequency in Hz
        duration (int): duration in seconds
    """
    winsound.Beep(frequency, duration * 1000)
