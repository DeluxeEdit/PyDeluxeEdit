from PyQt6.QtWidgets import QWidget, QTextEdit, QFormLayout, QTabWidget

class Tabs:
       
    def __init__(self):
        super().__init__()
        self.tabFiles = QTabWidget()
        self.allTabs=[]
    @property
    def currentTab(self):
        result=None
        index=self.tabFiles.currentIndex
        if index>=0:
             result=self.allTabs[index]

        return result

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
