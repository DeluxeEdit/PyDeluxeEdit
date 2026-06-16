import sys 
from PyQt6.QtWidgets import QApplication
from mymainwindow  import  MyMainWindow
from argparse import ArgumentParser

app = QApplication(sys.argv)

my = MyMainWindow()
parser = ArgumentParser(
                    prog='DeluxeEdit',
                    description='Advanced Text Editor',
                    epilog='Text at the bottom of help')

parser.add_argument('--hex', nargs='+', help='Whether we should do Hex View',default=False,dest='DoHexView')
parser.add_argument('path', nargs='?', help='Whanted path', default=None)
parsed = parser.parse_args()

if parsed.path:
    my.autoLoadFile(parsed.path,   parsed.DoHexView)



sys.exit(app.exec())
