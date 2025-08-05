import sys
from PySide6.QtWidgets import QApplication
from window import MainWindow
from PyQt6 import QtCore, QtGui
from window import Window

App = QtGui.QApplication(sys.argv)
     
#from PySide6.QtWidgets  import QApplication 
#App = QApplication(sys.argv)


#App = QApplication(sys.argv)
#App = QGuiApplication(s##ys.argv)

win=Window()
win.show()
App.exec()


QApplication.shutdown()
 