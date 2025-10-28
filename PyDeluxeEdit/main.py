import sys 
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtGui
from mainWidget import MainWidget       
        
#if __name__ == "__main__":
app = QApplication(sys.argv)
autoloadPath=None
autoLoadHex=False
# Below is command line handling,
argsLen=sys.argv.__len__()
if argsLen >=2:
    autoloadPath= sys.argv[1]  
    if argsLen>=3   and "--hex" in  sys.argv:  
        autoLoadHex=True
  
QApplication.setApplicationName('PyDeluxeEdit')
QApplication.setApplicationVersion('0.9.0')

mainWidget =MainWidget()
if autoloadPath:
    mainWidget.autoLoadFile(autoloadPath, autoLoadHex)
app.exec()

