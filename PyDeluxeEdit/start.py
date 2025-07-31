import sys
from PyQt6.QtWidgets import QGuiApplication 
from window import MainWindow


#app = QApplication(sys.argv)
App = QGuiApplication(sys.argv)

main=MainWindow()
main.show()
App.exec()


