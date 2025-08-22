
import sys
#from PySide6.QtCore import Qt
#from PySide6.QtWidgets import QApplication

from PyQt6.QtWidgets import QApplication

#if __name__ == "__main__":
app = QApplication(sys.argv)                                                     
    

from window import App
win=App()
# win.show()
app.exec()


 
