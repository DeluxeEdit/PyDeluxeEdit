from pydoc import text
from sqlite3 import connect
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QTextEdit
class MainWindow(QMainWindow):
    def handleFileChange(self):
        print("Text changed...>>> ")

    def __init__(self):
        super().__init__()    
    
    
    text=QTextEdit()
    text.textChanged.connect(handleFileChange())
        