from PyQt6.QtWidgets import QWidget, QTabWidget, QTextEdit, QMainWindow, QFormLayout
from PyQt6.QtGui import QIcon
class TextTabItem(QWidget):
  
    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        self.setLayout(layout)

        self.text = QTextEdit()
        self.text.textChanged.connect(self.handleFileChange)
        
        
        layout.addRow(self.text )
        self.text.setReadOnly(False)
        
    def handleFileChange(self, text):
        print("Text changed...>>> ")

    
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.tabFiles=QTabWidget()
        self.tab=TextTabItem() 
   
        self.setCentralWidget(self.tabFiles)

        self.tabFiles.addTab(self.tab,"Test")
        self.tabFiles.setTabText(0, "Changed")
        

      
    
        self.setWindowTitle("PyQt6 - Codeloop.org")
        # Set the window iconf
        self.setWindowIcon(QIcon("deluxeedit.png"))