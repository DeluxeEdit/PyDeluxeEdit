from curses.ascii import TAB
from pydoc import text
from sqlite3 import connect
from tokenize import tabsize
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QTextEdit,QTabWidget
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QIcon
import sys
# Define a class for the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def handleFileChange(self):
        print("Text changed...>>> ")
   

    
        

    tabFiles=QTabWidget()
    tab = QWidget(tabFiles)
    tabsize.addTab(tab,"Test")
          
    text=QTextEdit()
    text.textChanged.connect(handleFileChange())

    def __init__(self):
        super().__init__()
        
        # Set the geometry (position and size) of the window
        self.setGeometry(200,200, 700, 400)
        # Set the title of the window
        self.setWindowTitle("PyQt6 - Codeloop.org")
        # Set the window icon
        self.setWindowIcon(QIcon('deluxeedit.png-'))

# Create an instance of the QApplication
##
#app = QApplication(sys.argv)
# Create an instance of the Window class
window = MainWindow()
# Show th e window
 # Start the application event loop and exit when it's done
#sys.exit(app.exec())
        