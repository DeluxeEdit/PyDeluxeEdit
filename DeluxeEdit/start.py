import sys 
from PyQt6.QtWidgets import QApplication
from ui_mainWindow import  Ui_MainWindow
from argparse import ArgumentParser

QApplication.setApplicationName("DeluxeEdit")
QApplication.setApplicationVersion("0.9.0")

#if __name__ == "__main__":
app = QApplication(sys.argv)
ui = Ui_MainWindow()

parser =  ArgumentParser()

parser.add_argument("path",help="The desired path to open",default=None)
parser.add_argument(
    "--hex",
    dest="doHexView",
    help="Whether we should do Hex View.",default=False)
     
parsed_args = parser.parse_args()
    
#ui.setupUi()
if parsed_args.path:
    ui.autoLoadFile(parsed_args.path,parsed_args.doHexView)

sys.exit(app.exec())
