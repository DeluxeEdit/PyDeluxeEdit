import sys 
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtGui
#from MainWindow import Ui_MainWindow



#class MyMainWindow(QtGui.QMainWindow, clientGUI.Ui_MainWindow):
 #  def __init__(self):
  #      QtGui.QMainWindow.__init__(self)
   #     self.ui = clientGUI.Ui_MainWindow.setupUi(self)
        
        
app = QApplication(sys.argv)
#my=MyMainWindow()

       
from mainWidget import MainWidget
mainWidget =MainWidget()
app.exec()

