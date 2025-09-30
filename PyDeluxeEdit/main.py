import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from mainWidget import MainWidget
import mainWidget




#if __name__ == "__main__":
  
app = QApplication(sys.argv)



    


win=MainWidget()
win.show()
sys.exit(app.exec())



 
