from pydoc import text
from sqlite3 import connect
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit
class MainWindow(QMainWindow):
    def handleFileChange(self):
        print("Text changed...>>> ")

    def __init__(self):
        super().__init__()    
    
    app = QApplication(sys.argv)
    
    text=QTextEdit()
    text.textChanged.connect(handleFileChange())
        