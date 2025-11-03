from os import path
from typing import Self
from PyQt6.QtWidgets import QWidget, QMainWindow,QMenuBar, QMenu,QFileDialog, QStatusBar, QToolBar,QListWidget
from PyQt6 import uic   
from PyQt6.QtGui import QIcon, QAction
from models import TextTabItem, Tabs
from api import Api
from util import * 
class MainWidget(QMainWindow):

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
        
        self.status.showMessage("File:", filePath)
 
        
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



     
    def setMenu(self):
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        # Creating menus using a title

        newMenu = menuBar.addMenu("&New")
        editMenu = menuBar.addMenu("&Edit")
        saveMenu = menuBar.addMenu("&Save")
        saveAsMenu = menuBar.addMenu("Save As")
        registerMenu = menuBar.addMenu("Register Shell Extensions")
        aboutMenu = menuBar.addMenu("&About")
        # Creating menus using a QMenu object
        menuBar.addMenu(fileMenu)
        # Creating menus using a title
        newAction= QAction(self)
        aboutAction= QAction(self)
        registerAction= QAction(self)
        newAction.setShortcut("Ctrl+N")
        openAction = QAction(self)
        openAction.setShortcut("Ctrl+O")
        hexViewAction = QAction(self)
        hexViewAction.setShortcut("Ctrl+H")
        save = QAction(self)
        save.setShortcut("Ctrl+S")
        self.menuBar.show()
        
    def statusChanged(self,text):
        self.log.addItem(text)


      
    
    def __init__(self):

        super().__init__()

        self.window=uic.load_ui.loadUi(Api.ProjectUiFileName)
        
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        self.menuBar=QMenuBar()
        
       
        self.statusBar  = QStatusBar()
        self.statusBar.messageChanged.connect(self.statusChanged)
        self.statusBar.addPermanentWidget(self)
    
        toolbar = QToolBar("Log")
        log = QListWidget(self)
        toolbar.addWidget(log)
        self.addToolBar(toolbar)
        
        self.tabs=Tabs()
        self.setCentralWidget(self.tabs.tabFiles)
        self.api = Api()
        self.setMenu()
        
        self.window.show()





