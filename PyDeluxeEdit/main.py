import sys 
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtGui
from mainWidget import MainWidget       
        
#if __name__ == "__main__":
app = QApplication(sys.argv)
#my=MyMainWindow()

mainWidget =MainWidget()
mainWidget.loadProjectUi()
app.exec()

