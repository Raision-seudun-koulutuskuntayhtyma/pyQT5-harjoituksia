# ---SOUND GENERATOR GUI FULLY FUNCTIONAL---

# LIBRARIES AND MODULES

from PyQt5 import QtWidgets, uic # QT Libraries
import sys

from PyQt5.QtCore import left # For accessing arguments
import sound # Module for sound creation

# CLASS DEFINITIONS

# Class definition for the main window UI, slots & functions
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # Parent class init
        uic.loadUi("mainwindow.ui", self) # Loads the ui file

        # UI OBJECTS

        # Control Objects in the UI (inputs) 2 ways to create properties
        self.duration = self.durationSlider # Get the slider input object directly by using ui objectname, duration of the sound
        self.thousands = self.findChild(QtWidgets.QDial, 'kiloDial') # Get the dial input object by using pointer to ui objectname, khz part
        self.hundreds = self.findChild(QtWidgets.QDial, 'hundredDial') # Hundreds part
        self.tens = self.findChild(QtWidgets.QDial, 'tenDial') # Tens part
        self.ones = self.findChild(QtWidgets.QDial, 'oneDial') # Ones part

        # LCD indicator object
        self.lcd = self.findChild(QtWidgets.QLCDNumber, 'frequencyLcd') # The big 7 segment display
        
        # SIGNALS AND SLOTS

        # Connect playSound Button to the beep function by using ui objectName directly, event is clicked
        self.playSound.clicked.connect(self.beep) 
        
        # Connect dials to the big LCD with updateLcd function, event is valueChanged
        self.thousands.valueChanged.connect(self.updateLcd)
        self.hundreds.valueChanged.connect(self.updateLcd)
        self.tens.valueChanged.connect(self.updateLcd)
        self.ones.valueChanged.connect(self.updateLcd)
        
        # Connect Preset Menu Actions to dial setting funtion. Needs a lambda function to allow passing arguments (max 3)
        self.action1_kHz.triggered.connect(lambda: self.setDialsToPreset('1000')) # 1 kHz
        self.action100_Hz.triggered.connect(lambda: self.setDialsToPreset('0100')) # 100 Hz
        self.action666_Hz.triggered.connect(lambda: self.setDialsToPreset('0666')) # 666 Hz
        # MAKE THE UI VISIBLE
        self.show()


    # Numerical values extracted from dials and combined into frequency value (int)
    def frequency(self):
        freqThousands = self.thousands.value() * 1000 # Get value of the kHz dial and multiply it by 1000
        freqHundreds = self.hundreds.value() * 100 
        freqTens = self.tens.value() * 10
        freqOnes = self.ones.value()
        frequencyValue = freqThousands + freqHundreds + freqTens + freqOnes
        return frequencyValue

    
        
    # SLOT FUNCTIONS

    # Update the big LCD    
    def updateLcd(self):
        self.lcd.display(self.frequency())

    # Create the sound
    def beep(self):
        if self.frequency() < 37: # Frequency must be greater than 36 Hz
            print('Taajuuden on oltava vähintään 37 Hz') # Console logging
            # Create a notification dialog
            sound.warn_sound() # Warning sound
            notification = QtWidgets.QMessageBox()
            notification.setWindowTitle('Virheellinen taajuus')
            notification.setText('Taajuuden pitää olla vähintään 37 Hz!')
            notification.exec_()
            
            # Set dials ten and ones to 3 and 7 for the minimum frequency
            self.tens.setValue(3)
            self.ones.setValue(7)
        else: 
            sound.create_sound(self.frequency(), self.duration.value()) 

    # Method to set all 4 dials according to a preset
    def setDialsToPreset(self, presetText):
        d1 = presetText[0] # First dial (kHz)
        d2 = presetText[1]
        d3= presetText[2]
        d4 = presetText[3] # Last dial (Hz)

        self.thousands.setValue(int(d1))
        self.hundreds.setValue(int(d2))
        self.tens.setValue(int(d3))
        self.ones.setValue(int(d4))

    # Function for testing extraction of values from slider & dials 
    def echoConsole(self):
        print('Taajuus on ' + str(self.frequency()) + ' Hz ja kesto on ' + str(self.duration.value()) + ' s')
      

# CREATE AND RUN THE APP
app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.setWindowTitle('Äänigeneraattori')
app.exec_()
