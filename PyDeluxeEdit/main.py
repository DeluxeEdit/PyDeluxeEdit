import sys 
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtGui
from mainWidget import MainWidget       
        
#if __name__ == "__main__":
app = QApplication(sys.argv)
if sys.argv.count>=1:
    autoloadPath= sys.argv[0]
    
if sys.argv.count>=2  and sys.argv in "hex":
    autoLoadHex=True
    
#my=MyMainWindow()
mainWidget =MainWidget()
if autoloadPath.__len__ >0:
    mainWidget.autoLoadFile(autoloadPath, autoLoadHex)
mainWidget.loadProjectUi()
app.exec()

