#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 04:50:02 2016

@author: jafrey
"""
from PyQt5.uic import loadUiType
from PyQt5 import QtWidgets
import sys

Ui_MainWindow, QMainWindow = loadUiType('control_gui.ui')
        
class MainWindow(QMainWindow, Ui_MainWindow):  
#class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        
        self.setupUi(self)
        self.pushButton.clicked.connect(self.browse_folder)
        self.actionAbout.triggered.connect(self.browse_folder)
        self.statusBar().showMessage("", 5000)
        #self.pushButton.clicked.connect(self.actionAbout)
        
    def browse_folder(self,):
        QtWidgets.QMessageBox.about(self, "About", """Copyright 2016 Jed Frey""")
    def actionAbout(self):
        print("Hello World")
        
    
    def actionEaster_Eggs(self,):
        print("Hello Easter Egg")
 #       QtWidgets.QMessageBox.about(self, "About",
#                                    """Copyright 2016 Jed Frey
#                                This program is a simple GUI example for controls.""")
        
   
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    main = MainWindow() 
    main.show()
    sys.exit(app.exec_())