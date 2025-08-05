from pydoc import text
from sqlite3 import connect
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QTextEdit
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

# Define a class for the main window
class Window(QWidget):
    def handleFileChange(self):
        print("Text changed...>>> ")

    text=QTextEdit()
    text.textChanged.connect(handleFileChange())

    def __init__(self):
        super().__init__()
        
        # Set the geometry (position and size) of the window
        self.setGeometry(200,200, 700, 400)
        # Set the title of the window
        self.setWindowTitle("PyQt6 - Codeloop.org")
        # Set the window icon
        self.setWindowIcon(QIcon('deluxeedit.png'))

# Create an instance of the QApplication
app = QApplication(sys.argv)
# Create an instance of the Window class
window = Window()
# Show the window
window.show()
# Start the application event loop and exit when it's done
sys.exit(app.exec())
        