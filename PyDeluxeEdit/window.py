from PySide6.QtWidgets import QMainWindow, QTextEdit,QTabWidget
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QIcon
import sys
# Define a class for the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 - Codeloop.org")
        # Set the window icon
        self.setWindowIcon(QIcon("deluxeedit.png"))
    
    def handleFileChange(self):
        print("Text changed...>>> ")
   

    
        

    tabFiles=QTabWidget()
    tab = QWidget(tabFiles)
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
window = MainWindow()
# Show th e window
 # Start the application event loop and exit when it's done
#sys.exit(app.exec())
        