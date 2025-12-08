import sys 
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtGui
from mainWidget import MainWidget       
from PyQt6.QtWidgets import QMainWindow
from ui_mainwindow import  Ui_MainWindow
        
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

ui = Ui_MainWindow()
ui.setupUi()
    

if autoloadPath:
    ui.autoLoadFile(autoloadPath, autoLoadHex)
app.exec()

