import sys
from PySide6.QtWidgets import QApplication, QTextEdit
from PySide6.QtCore import Slot

@Slot()
def  handleTestChange():
    print("Button clicked, Hello!")

# Create the Qt Application
app = QApplication(sys.argv)
# Create a button, connect it and show it
text=QTextEdit()
text.changeEvent(handleTestChange)
# Run the main Qt loop
app.exec()