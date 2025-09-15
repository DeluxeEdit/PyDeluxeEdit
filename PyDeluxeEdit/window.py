from fileinput import filename
from os import path
from tkinter.filedialog import SaveFileDialog
from typing import Self
from PyQt6.QtWidgets import QWidget, QTabWidget, QTextEdit, QMainWindow, QFormLayout,QMenuBar, QFileDialog
from PyQt6.QtGui import QIcon, QAction
from api import Api
class TextTabItem(QWidget):
    
    def onTextChanged(text):
        print("Text changed.>>> ")
   
    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        self.setLayout(layout)
        self.text = QTextEdit()
        layout.addRow(self.text)
        self.text.textChanged.connect(self.onTextChanged)
        
                
    
class App(QMainWindow):
    def addFile(path,hexView=False):
        tab=TextTabItem() 
        Self.tabFiles.addTab(tab,path)
        tab.text=Self.api.loadFile(path,hexView)
    def openFileDialog(self):
        dialog = QFileDialog(self)
        #dialog.setDirectory(r"C:\")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("All files (*.*)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            if dialog.selectedFiles().length ==1:
                file=dialog.selectedFiles()[0]
                Self.addFile(path)
   
    def saveAsDialog(self):
        file = QFileDialog.getSaveFileName(self, "Save File", "All Files(*);;Text Files(*.txt)")
        if file:      
            
            def doHexView(path):
                Self.addFile(path, True)

        def setMenu():
            bar = QMenuBar()
            file = bar.addMenu("File")
            file.addAction("New")
            openMenu = QAction("Open")
            openMenu.setShortcut("Ctrl+O")
            hexViewMenu = QAction("Hex view")
            hexViewMenu.setShortcut("Ctrl+H")
            save = QAction("Save")
            save.setShortcut("Ctrl+S")
            file.addAction(save, Self.saveAsDialog)
            file.addAction(openMenu, Self.openFileDialog)
            file.addAction(hexViewMenu, Self.doHexView)

        def __init__(self):
                super().__init__()
        
                self.tabFiles=QTabWidget()
   
                self.setCentralWidget(self.tabFiles)

                self.api=Api()  
                setMenu()
    
                self.setWindowTitle("PyQt6 - Codeloop.org")
                # Set the window iconf
                self.setWindowIcon(QIcon("deluxeedit.png"))



          