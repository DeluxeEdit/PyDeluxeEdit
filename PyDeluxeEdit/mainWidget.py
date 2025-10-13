from os import path
from typing import Self
from PyQt6.QtWidgets import QWidget, QMainWindow,QMenuBar, QFileDialog, QStatusBar, QToolBar,QListWidget, uic
from PyQt6 import uic  
from PyQt6.QtGui import QIcon, QAction
from models import TextTabItem, Tabs
from api import Api

class MainWidget(QMainWindow):

      
    def addFile(filePath, hexView=False, isNewFile=False):
        tab = TextTabItem()
        tab.filePath=filePath
        Self.tabFiles.addTab(tab, path.basename(filePath))
        Self.tabs.allTabs.append(tab)
        if  isNewFile:
            tab.isNewFile=True
        else:
            tab.text.append(Self.api.loadFil3e(filePath, hexView))
        
        Self.status.showMessage("File:", filePath)
 
        
    def showNewFileDialog():
        dialog = QFileDialog(Self)
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        dialog.setNameFilter("New File", "All files (*.*)")
        if dialog.exec():
            filePath = dialog.selectFile
            Self.addFile(filePath, False, True)
               

    def openFileDialog(hexView=False):
        dialog = QFileDialog(Self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Open File", "All files (*.*)")
        if dialog.exec():
                filePath = dialog.selectFile
                Self. addFile(filePath, hexView)

    def saveAsDialog():
        filePath = QFileDialog.getSaveFileName(Self, "Save File", "All Files(*);;Text Files(*.txt)")
        if filePath:
            Self.api.saveFile(filePath,Self.tabs.currentTab.text.document().toRawText())
            
    def doHexView():
        Self.openFileDialog(True)
    


     
    
    def setMenu():
      
        file =Self.menuBar.addMenu("File")
        newMenu= QAction("New")
        newMenu.setShortcut("Ctrl+N")
        openMenu = QAction("Open")
        openMenu.setShortcut("Ctrl+O")
        hexViewMenu = QAction("Hex view")
        hexViewMenu.setShortcut("Ctrl+H")
        save = QAction("Save")
        save.setShortcut("Ctrl+S")
        file.addAction(save, Self.saveAsDialog)
        file.addAction(openMenu, Self.openFileDialog)
        file.addAction(hexViewMenu, Self.doHexView)
        file.addAction(newMenu, Self.showNewFileDialog)
        Self.menuBar.show()

    def statusChanged(text):
        Self.log.addItem(text)
    
    def loadProjectUi(showToo=False):
        uic.load_ui(Api.ProjectUiFileName)
        if showToo:
          Self.show()

    def __init__(self):
        super().__init__()
        self.menuBar=QMenuBar()
        
       
        self.statusBar  = QStatusBar()
        self.statusBar.messageChanged.connect(self.statusChanged)
        self.statusBar.addPermanentWidget(self)
    
        toolbar = QToolBar("Log")
        log = QListWidget(self)
        toolbar.addWidget(log)
        self.addToolBar(self.toolbar)
        
        self.tabs=Tabs()
        self.setCentralWidget(self.tabs.tabFiles)
        self.api = Api()
        self.setMenu
      
        #self.window.show()



