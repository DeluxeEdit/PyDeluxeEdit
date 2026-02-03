import sys 
from PyQt6.QtWidgets import QApplication
from myMainWindow import  MyMainWindow

QApplication.setApplicationName("DeluxeEdit")
QApplication.setApplicationVersion("0.9.0")

#if __name__ == "__main__":
app = QApplication(sys.argv)
my = MyMainWindow()
argsLen=len(sys.argv)

if argsLen>1:
    autoloadPath= sys.argv[0]
    if argsLen>=2  and sys.argv in "--hex":
        AutoLoadHex=True
    my.autoLoadFile(autoloadPath,AutoLoadHex)

sys.exit(app.exec())
