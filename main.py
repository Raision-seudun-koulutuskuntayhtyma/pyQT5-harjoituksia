# SOUND GENERATOR

# Libraries and modules

from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication

import sound 

# GUI Initalisation
Form, Window = uic.loadUiType("mainwindow.ui")

# Create UI objects
app = QApplication([])
window = Window()
form = Form()

# Setup and show the window
form.setupUi(window)
window.show()

# Start the application
app.exec()