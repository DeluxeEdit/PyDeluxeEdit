import sys
from PySide6.QtWidgets import QApplication
from window import MainWindow
class Start():
    def doStart():
        app = QApplication(sys.argv)
        win=MainWindow()
        win.show()
        app.exec()


