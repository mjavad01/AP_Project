import os
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar2QT
from matplotlib.figure import Figure
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
import numpy as np

Form = uic.loadUiType(os.path.join(os.getcwd(), "Form.ui"))[0]

class IntroWindows(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resizeButton.clicked.connect(self.say)
        self.thread = None
    
    def say(self):
        print("Hello")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = IntroWindows()
    window.show()
    app.exec_()
    sys.exit(app.exec_())