import sys 
from PyQt6.QtWidgets import QApplication

from mainWidget import MainWidget
if __name__ == "__main__":
    app = QApplication(sys.argv)

       

   
    mainWidget =MainWidget()
    mainWidget.show
    app.exec()

