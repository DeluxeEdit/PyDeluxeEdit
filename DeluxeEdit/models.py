from PyQt6.QtWidgets import QWidget, QTextEdit, QFormLayout, QTabWidget, QLabel,QApplication

class Tabs:

    @property
    def currentTab(self):
        result=None
        index=self.tabFiles.currentIndex()
        if index>=0:
                result=self.allTabs[index]

        return result

    def __init__(self):
        super().__init__()
        self.tabFiles = QTabWidget()
        self.allTabs=[]
   
    
class TextTabItem(QWidget):

    def onTextChanged(text):
        print("Text changed.>>> ")

    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        self.setLayout(layout)
        self.text = QTextEdit
        
        self.text.autoFormatting=True
        self.filePath=None
        self.isNewFile=False
        layout.addRow(self.text)
        self.text.textChanged.connect(self.onTextChanged)

class About(QWidget):

    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        self.setLayout(layout)
        self.applicationName = QLabel
        self.applicationVersion=QLabel
        self.applicationName= QApplication.applicationName
        self.applicationVersion= QApplication.applicationVersion
