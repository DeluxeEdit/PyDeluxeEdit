import sys
#from PySide6.QtCore import Qt

#from PySide6.QtWidgets import QApplication

from PyQt6.QtWidgets import QApplication
from mainWindow import MainWindow

def main():
    app = QApplication(sys.argv)                                                     
    win=MainWindow()
    win.show()

    app.exec()
if __name__ == "__main__":
    main()












    89
   


 
