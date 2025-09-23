from PyQt6.QtWidgets import QWidget, QTextEdit, QFormLayout

class TextTabItem(QWidget):

    def onTextChanged(text):
        print("Text changed.>>> ")

    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        self.setLayout(layout)
        self.text = QTextEdit()
        self.text.autoFormatting=True
        self.filePath=None
        layout.addRow(self.text)
        self.text.textChanged.connect(self.onTextChanged)
