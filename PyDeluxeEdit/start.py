import sys
from PyQt5 import QtWidgets
     
#from PySide6.QtWidgets  import QApplication 
from window import MainWindow
App = QtWidgets.QApplication(sys.argv)


#App = QApplication(sys.argv)
#App = QGuiApplication(s##ys.argv)

main=MainWindow()
main.show()
App.exec()


