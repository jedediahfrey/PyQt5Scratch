#!/usr/bin/env python3

from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtWidgets
import sys

import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

Ui_MainWindow, QMainWindow = loadUiType('window2.ui')
#from window2 import Ui_MainWindow

from scipy import signal

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.verticalLayout.addWidget(self.canvas)
        
        self.toolbar = NavigationToolbar(self.canvas, self.widget, coordinates=True)
        self.verticalLayout.addWidget(self.toolbar)
        
        self.plotButton.clicked.connect(self.makeplot)
        
    def makeplot(self):
         print("Hello World")
         K = self.gain.value()
         tau = self.tau.value()

         sys = signal.TransferFunction([K],[tau,1])
         T, yout = signal.step(sys)
         self.ax.clear()
         self.ax.plot(T,yout)
         self.canvas.draw()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    main = MainWindow() 
    main.show()
    sys.exit(app.exec_())
