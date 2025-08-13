from PyQt6.QtWidgets import QWidget, QTabWidget, QTextEdit, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 - Codeloop.org")
        # Set the window icon
        self.setWindowIcon(QIcon("deluxeedit.png"))
    
    def handleFileChange(self):
        print("Text changed...>>> ")
   
        
    tabFiles=QTabWidget()
    tab=QWidget(tabFiles,Qt.Window)
    tab.text=QTextEdit()
    tab.text.textChanged.connect(handleFileChange())
    
    tabFiles.addTab(tab,"Test")
    tabFiles.setTabText(0, "Changed")         

        
        # Set the geometry (position and size) of the window
        # Set the title of the window


# Create an instance of the QApplication
##
#app = QApplication(sys.argv)
# Create an instance of the Window class
# Show th e window
 # Start the application event loop and exit when it's done
#sys.exit(app.exec())
        