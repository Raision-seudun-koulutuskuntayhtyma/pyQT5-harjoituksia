# SOUND GENERATOR GUI FULLY FUNCTIONAL

# Libraries and modules

from PyQt5 import QtWidgets, uic # QT Libraries
import sys # For accessing arguments
import sound # Module for sound creation

# Class definition for the main window UI, slots & functions
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # Parent class init
        uic.loadUi("mainwindow.ui", self) # Loads the ui file

        # Control Objects in the UI (inputs)
        self.duration = self.durationSlider # Get the slider input object directly by using ui objectname, duration of the sound
        self.thousands = self.findChild(QtWidgets.QDial, 'kiloDial') # Get the dial input object by using pointer to ui objectname, khz part
        self.hundreds = self.findChild(QtWidgets.QDial, 'hundredDial') # Hundreds part
        self.tens = self.findChild(QtWidgets.QDial, 'tenDial') # Tens part
        self.ones = self.findChild(QtWidgets.QDial, 'oneDial') # Ones part

        # LCD indicator object
        self.lcd = self.findChild(QtWidgets.QLCDNumber, 'frequencyLcd') # The big 7 segment display
        
        # Signals and slots
        self.playSound.clicked.connect(self.echoConsole) # Connect Button playSound to beep function by using directly ui objectName

        # Make the UI visible
        self.show() 

    def frequency(self):
        # Numerical values extracted from dials and combined into frequency value
        freqThousands = self.thousands.value() # Get value of the kHz dial and multiply it by 1000
        freqHundreds = self.hundreds.value() * 100
        freqTens = self.tens.value() * 10
        freqOnes = self.ones.value()
        frequencyValue = freqThousands + freqHundreds + freqTens + freqOnes
        return frequencyValue

    # Slot functions
    def beep(self):
        sound.create_sound(self.frequencyValue, self.durationValue)       

    def echoConsole(self):
        print('Arvo on ' + str(frequency())) # For testing purposes only

# Create the app
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
