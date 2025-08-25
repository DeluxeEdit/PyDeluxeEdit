from typing import Self
from PyQt6.QtWidgets import QWidget, QTabWidget, QTextEdit, QMainWindow, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

from PyQt6.QtWidgets import QWidget, QTabWidget, QTextEdit, QMainWindow


class App(QMainWindow):
    def handleFileChange(self, text):
        print("Text changed...>>> ")

    def __init__(self):
        super().__init__()
        self.tab = QWidget(self.tabFiles)
        self.tab.text = QTextEdit()
        self.tab.text.textChanged.connect(self.handleFileChange)
        
        self.setCentralWidget(self.tabFiles)
        
        vertical= QVBoxLayout()
        vertical.addWidget(self.tab)  # Spacer

        self.setLayout(vertical)

    
    
        self.tabFiles = QTabWidget()
        
        self.tabFiles.addTab(self.tab, "Test")
        self.tabFiles.setTabText(0, "Changed")

        self.setWindowTitle("PyQt6 - Codeloop.org")
        # Set the window iconf
        self.setWindowIcon(QIcon("deluxeedit.png"))