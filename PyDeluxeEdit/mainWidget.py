from os import path
from PyQt6.QtWidgets import QWidget, QMainWindow,QMenuBar, QMenu,QFileDialog, QStatusBar, QToolBar,QListWidget
from PyQt6 import uic   
from PyQt6.QtGui import QIcon, QAction
from models import TextTabItem, Tabs
from api import Api
from util import *
 #"from PySid.QtUiTools import QUiLoader
class MainWidget(QWidget):

    def autoLoadFile(self, filePath, hexView=False):
      self.addFile(filePath, hexView)

    def addFile(self,filePath, hexView=False, isNewFile=False):
        tab = TextTabItem()
        tab.filePath=filePath
        self.tabFiles.addTab(tab, path.basename(filePath))
        self.tabs.allTabs.append(tab)
        if  isNewFile:
            tab.isNewFile=True
        else:
            tab.text.append(self.api.loadFile(filePath, hexView))
        
        self.statusBar.showMessage("File:", filePath)
 
        
    def showNewFileDialog(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        dialog.setNameFilter("New File", "All files (*.*)")
        if dialog.exec():
            filePath = dialog.selectFile
            self.addFile(filePath, False, True)
               

    def openFileDialog(self,hexView=False):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Open File", "All files (*.*)")
        if dialog.exec():
                filePath = dialog.selectFile
                self. addFile(filePath, hexView)

    def saveAsDialog(self):
        filePath = QFileDialog.getSaveFileName(self, "Save File", "All Files(*);;Text Files(*.txt)")
        if filePath:
            self.api.saveFile(filePath,self.tabs.currentTab.text.document().toRawText())
            
    def doHexView(self):
        self.openFileDialog(True)
  
    def registerShellExtesions(self):
        Util.ExecuteShell("powershell.exe register.ps1")



   


      
    
    def __init__(self, status):
        self.statusBar  =status

        super().__init__()

     #   self.window.ui.setupUi(self);                        
    #    self.window=uic.load_ui.loadUi(Api.ProjectUiFileName)
        





