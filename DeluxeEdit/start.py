import sys 
from PyQt6.QtWidgets import QApplication
from myMainWindow import  MyMainWindow
from argparse import ArgumentParser

QApplication.setApplicationName("DeluxeEdit")
QApplication.setApplicationVersion("0.9.0")

#if __name__ == "__main__":
app = QApplication(sys.argv)
my = MyMainWindow()

parser =  ArgumentParser()

parser.add_argument("path",None,None,None,None ,None, None,False,"The desired path to open.",None,None)
""""
    help="The desired path to open.",
    required=False,
    default=None)

parser.add_argument(
    "--hex",
    help="Whether we should do Hex View",
    required=False,
    default=False,
    dest="doHexView"
    )

"""
parsed_args = parser.parse_args()
if parsed_args.path:
    my.autoLoadFile(parsed_args.path,parsed_args.doHexView)

sys.exit(app.exec())
