from fileinput import filename
from PyQt6.QtWidgets import QWidget, QTabWidget, QTextEdit, QMainWindow, QFormLayout,QMenuBar, QFileDialog
from PyQt6.QtGui import QIcon, QAction
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
    def __init__(self):
        super().__init__()
        
        self.tabFiles=QTabWidget()
        self.tab=TextTabItem() 
   
        self.setCentralWidget(self.tabFiles)

        self.tabFiles.addTab(self.tab,"Test")
        self.tabFiles.setTabText(0, "Changed")
        self.tab.text

      
    
        self.setWindowTitle("PyQt6 - Codeloop.org")
        # Set the window iconf
        self.setWindowIcon(QIcon("deluxeedit.png"))
   
    def openFileDialog(self):
        dialog = QFileDialog(self)
        #dialog.setDirectory(r"C:\")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("All files (*.*)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
                 if dialog.selectedFiles().length ==1:
                     fileName=dialog.selectedFiles()[0]
    
    def saveAsDialog(self):
        fileName = QFileDialog.getSaveFileName(self, "Save File", "All Files(*);;Text Files(*.txt)")
        if fileName:      
            saveF
    
    def setMenu():
        bar = QMenuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        openMenu = QAction("Open")
        openMenu.setShortcut("Ctrl+O")
        save = QAction("Save")
        save.setShortcut("Ctrl+S")
        file.addAction(save, saveFile)
