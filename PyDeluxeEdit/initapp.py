import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)                                                     
    

from window import MainWindow
win=MainWindow()
win.show()
app.exec()


 
