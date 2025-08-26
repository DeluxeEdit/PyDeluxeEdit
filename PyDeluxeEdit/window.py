from PyQt6.QtWidgets import QWidget, QTabWidget, QTextEdit, QMainWindow, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys

from PyQt6.QtWidgets import QWidget, QTabWidget, QTextEdit, QMainWindow
class TextTabItem(QWidget):
    text = QTextEdit()
 
class App(QMainWindow):
  
    def handleFileChange(self, text):
        print("Text changed...>>> ")

    def __init__(self):
        super().__init__()
        self.tabFiles=QTabWidget()
   
        self.tab=TextTabItem() 
        #
        #self.tab.text.textChanged.connect(self.handleFileChange)
        
        self.setCentralWidget(self.tabFiles)

        self.tabFiles.addTab(self.tab,"Test")
        self.tabFiles.setTabText(0, "Changed")
        

        #self.setLayout(self.layout)

   
    
        self.setWindowTitle("PyQt6 - Codeloop.org")
        # Set the window iconf
        self.setWindowIcon(QIcon("deluxeedit.png"))