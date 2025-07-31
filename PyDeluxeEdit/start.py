import sys
from PySide6.QtWidgets import QApplication
from window import MainWindow
class Start():
    def _init__(self):
        app = QApplication(sys.argv)
        main=MainWindow()
        main.show()

Start()        


