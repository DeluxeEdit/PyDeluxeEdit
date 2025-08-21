from PyQt6.QtWidgets import QWidget, QTabWidget, QTextEdit, QMainWindow, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

from PyQt6.QtWidgets import QWidget, QTabWidget, QTextEdit, QMainWindow
class App(QMainWindow):
    def handleFileChange(self,text):
        print("Text changed...>>> ")
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        

        self.tabFiles=QTabWidget()
        self.tabFiles.setVisible(True)
        self.tab=QWidget(self.tabFiles)
        self.tab.text=QTextEdit()
        self.tab.text.textChanged.connect( self.handleFileChange)
    

        self.layout.addWidget(self.tabFiles)
        self.layout.addWidget( self.tab.text)
        self.tabFiles.addTab(self.tab,"Test")
        self.tabFiles.setTabText(0, "Changed")         
   #     self.setGeometry(10,10, 500, 500)
        self.layout.a (self.tabFiles)
        self.layout.addWidget(self.tab.text)

        self.setWindowTitle("PyQt6 - Codeloop.org")
        # Set the window icon
        self.setWindowIcon(QIcon("deluxeedit.png"))
        self.show()

   
            