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
        # Play Sound button
        self.playSound.clicked.connect(self.tone)  

        # Dials
        self.thousands.valueChanged.connect(self.updateLcd)
        self.hundreds.valueChanged.connect(self.updateLcd)
        self.tens.valueChanged.connect(self.updateLcd)
        self.ones.valueChanged.connect(self.updateLcd)

        # Menu actions
        self.action1_kHz.triggered.connect(lambda: self.loadPreset(1, 0, 0, 0))
        self.action100_Hz.triggered.connect(lambda: self.loadPreset(0, 1, 0, 0))
        self.action666_Hz.triggered.connect(lambda: self.loadPreset(0, 6, 6, 6))
        # MAKE UI VISIBLE
        self.show()

    # METHODS
    # Play sound
    def tone(self):
        if self.calculateFrequency() < 37:
            sound.warn_sound()
            alarmWindow = QtWidgets.QMessageBox()
            alarmWindow.setText('Frequency shoud be 37 Hz at minimum')
            alarmWindow.setWindowTitle('Frequency error')
            alarmWindow.exec_()

            # Set the minimum allowed value
            self.tens.setValue(3)
            self.ones.setValue(7)

        else:        
            sound.create_sound(self.calculateFrequency(), self.duration.value())

    # Calculate frequency
    def calculateFrequency(self):
        fthousands = self.thousands.value() * 1000
        fhundreds = self.hundreds.value() * 100
        ftens = self.tens.value() * 10
        fones = self.ones.value()
        frequency = fthousands + fhundreds + ftens + fones 
        return frequency

    # Update the LCD
    def updateLcd(self):
        self.bigLcd.display(self.calculateFrequency())

    # Load preset
    def loadPreset(self, d1, d2, d3, d4):
        self.thousands.setValue(d1)
        self.hundreds.setValue(d2)
        self.tens.setValue(d3)
        self.ones.setValue(d4)

# CREATE & RUN UI

app = QtWidgets.QApplication(sys.argv)
mainwindow = Ui()
app.exec_()
       