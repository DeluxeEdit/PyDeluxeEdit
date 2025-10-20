import sys 
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtGui
from mainWidget import MainWidget       
        
#if __name__ == "__main__":
app = QApplication(sys.argv)

# Below is command line handling,
if sys.argv.count>=1:
    autoloadPath= sys.argv[0]   
if sys.argv.count>=2   and "--hex" in  sys.argv:  
    autoLoadHex=True
    
#my=MyMainWindow()
mainWidget =MainWidget()
if autoloadPath:
    mainWidget.autoLoadFile(autoloadPath, autoLoadHex)
app.exec()

