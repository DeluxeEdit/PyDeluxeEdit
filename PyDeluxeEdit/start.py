import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit
class MainWindow(QMainWindow):
    @Slot(str)
    def handleTextChange(self, text: str):
        print("Button clicked, Hello!")

    # Create the Qt Application
    app = QApplication(sys.argv)
    
    # Create a button, connect it and show it
    text=QTextEdit()
    text.changeEvent(handleTextChange)
# Run the main Qt loop
