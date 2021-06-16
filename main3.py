# --- HEADPHONES TESTING APPLICATION ---

# LIBRARIES AND MODULES
from PyQt5 import QtWidgets, uic 
import sys # For accessing system parameters
import sound # Our home brew sound library

# CLASS DEFINITIONS

# Class for the main window
class Ui(QtWidgets.QMainWindow):

    # CONSTRUCTOR
    def __init__(self):
        super().__init__()

        # Load the ui file
        uic.loadUi('mainwindow.ui', self)

        # UI OBJECTS
        # Controls
        self.duration = self.durationSlider # Direct assignment
        self.thousands = self.findChild(QtWidgets.QDial, 'kiloDial') # Assignment by pointer
        self.hundreds = self.findChild(QtWidgets.QDial, 'hundredDial')
        self.tens = self.findChild(QtWidgets.QDial, 'tenDial')
        self.ones = self.findChild(QtWidgets.QDial, 'oneDial')

        # Indicators
        self.bigLcd = self.findChild(QtWidgets.QLCDNumber , 'frequencyLcd')

        # SIGNALS & SLOTS
        self.playSound.clicked.connect(self.tone)
        
        # MAKE UI VISIBLE
        self.show()

    # METHODS
    # Play sound
    def tone(self):
        sound.create_sound(500, 1)

    # Calculate frequency
    def calculateFrequency(self):
        pass

    # Update the LCD
    def updateLcd(self):
        pass

    # Load preset
    def loadPreset(self):
        pass

# CREATE & RUN UI

app = QtWidgets.QApplication(sys.argv)
mainwindow = Ui()
app.exec_()
       