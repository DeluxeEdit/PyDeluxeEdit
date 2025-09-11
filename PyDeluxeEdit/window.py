from fileinput import filename
from os import path
from tkinter.filedialog import SaveFileDialog
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
    def openFileDialog(self):
        dialog = QFileDialog(self)
        #dialog.setDirectory(r"C:\")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("All files (*.*)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            if dialog.selectedFiles().length ==1:
                file=dialog.selectedFiles()[0]
                self.api.loadFile(file)
    
   
    def saveAsDialog(self):
        file = QFileDialog.getSaveFileName(self, "Save File", "All Files(*);;Text Files(*.txt)")
        if file:      
            
    
            def setMenu():
                bar = QMenuBar()
                file = bar.addMenu("File")
                file.addAction("New")
                openMenu = QAction("Open")
                openMenu.setShortcut("Ctrl+O")
                save = QAction("Save")
                save.setShortcut("Ctrl+S")
                file.addAction(save, self.saveAsDialog)
                file.addAction(openMenu, self.openFileDialog)

            def __init__(self):
                super().__init__()
        
                self.tabFiles=QTabWidget()
   
                self.setCentralWidget(self.tabFiles)

                self.api=Api()
                setMenu()
    
        self.setWindowTitle("PyQt6 - Codeloop.org")
        # Set the window iconf
        self.setWindowIcon(QIcon("deluxeedit.png"))

    def addFile(path,hexView=False):
        tab=TextTabItem() 
        self.tabFiles.addTab(tab,path)
  
       
   