from os import path
from re import A
from typing import Self
from PyQt6.QtWidgets import QWidget, QMainWindow,QMenuBar, QMenu,QFileDialog, QStatusBar, QToolBar,QListWidget
from PyQt6 import uic   
from PyQt6.QtGui import QIcon, QAction
from models import TextTabItem, Tabs
from api import Api
from util import *
from layout import Ui_MainWindow
 #"from PySid.QtUiTools import QUiLoader
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
        menuBar = self.menuBar
        # Creating menus
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        """
        my=menuBar.addMenu("&New")
        newMenu = QMenu("&New", fileMenu)
        editMenu = QMenu("&Edit", fileMenu )
        saveMenu = QMenu("&Save",fileMenu)
        saveAsMenu = QMenu("Save As", fileMenu)
        registerMenu = QMenu("Register Shell Extensions", fileMenu)
        aboutMenu = QMenu("&About", fileMenu)
        
        menuBar.addMenu(newMenu)
        menuBar.addMenu(editMenu)
        menuBar.addMenu(saveMenu)
        menuBar.addMenu(saveAsMenu)
        menuBar.addMenu(registerMenu)
        menuBar.addMenu(aboutMenu)
        
       # Creating menus using a QMenu object
      
       """
       # Creating actions
        newAction= QAction("New")
        aboutAction= QAction(self)
        registerAction= QAction(self)
        newAction.setShortcut("Ctrl+N")
        openAction = QAction(self)
        openAction.setShortcut("Ctrl+O")
        hexViewAction = QAction(self)
        hexViewAction.setShortcut("Ctrl+H")
        saveAction = QAction(self)
        saveAction.setShortcut("Ctrl+S")
        saveAsAction = QAction(self)
        """
        # adding actions
        newMenu.addAction(newAction )
        editMenu.addAction(openAction )
        saveMenu.addAction(saveAction )
        saveAsMenu.addAction(saveAsAction )
        newMenu.addAction(newAction )
        registerMenu.addAction(newAction )
        aboutMenu.addAction(aboutAction)
""" 
        # Creating connection between
        newAction.triggered.connect(self.showNewFileDialog)
        menuBar.show()
        
    def statusChanged(self,text):
        self.log.addItem(text)


      
    
    def __init__(self):

        super().__init__()

     #   self.window.ui.setupUi(self);                        
        menuBar = QMenuBar()
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
        self.window=uic.load_ui.loadUi(Api.ProjectUiFileName)
        
        self.window.show()





