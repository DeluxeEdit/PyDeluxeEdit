from os import path
from typing import Self
from PyQt6.QtWidgets import QWidget,QTabWidget, QMainWindow,QMenuBar, QFileDialog, QStatusBar, QToolBar,QListWidget
from PyQt6.QtGui import QIcon, QAction
from models import TextTabItem, Tabs
from api import Api

class MainWidget(QWidget):
    QMainWindow

    def addAndLoadFile(filePath, hexView=False, isNewFile=False):
        tab = TextTabItem()
        tab.filePath=filePath
        Self.tabFiles.addTab(tab, path.basename(filePath))
        Self.tabs.allTabs.append(tab)
        if  isNewFile:
            tab.isNewFile=True
        else:
            tab.text.append(Self.api.loadFil3e(filePath, hexView))
        
        Self.status.showMessage("File:", filePath)
    
    def doNewFile(filePath):
        tab = TextTabItem()
        tab.filePath=filePath
       
        Self.tabFiles.addTab(tab, path.basename(filePath))
        Self.tabs.allTabs.append(tab)
        
    def newFileDialog():
        dialog = QFileDialog(Self)
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        dialog.setNameFilter("New File", "All files (*.*)")
        if dialog.exec():
            filePath = dialog.selectFile
            Self.addAndLoadFile(filePath, False, True)
               

    def openFileDialog(hexView=False):
        dialog = QFileDialog(Self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Open File", "All files (*.*)")
        if dialog.exec():
                filePath = dialog.selectFile
                Self. addAndLoadFile(filePath, hexView)

    def saveAsDialog():
        filePath = QFileDialog.getSaveFileName(Self, "Save File", "All Files(*);;Text Files(*.txt)")
        if filePath:
            Self.api.saveFile(filePath,Self.tabs.currentTab.text.document().toRawText())
            
    def doHexView():
        Self.openFileDialog(True)
    


     
    
    def setMenu():
        bar = QMenuBar()
        file = bar.addMenu("File")
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
        file.addAction(newMenu, Self.newFileDialog)
        bar.show()
    def statusChanged(text):
        Self.log.addItem(text)

    def __init__(self):
        super().__init__()

        win=QMainWindow()
        self.window=win

        self.status = QStatusBar()
        self.status.messageChanged.connect(self.statusChanged)
        self.status.addPermanentWidget(self)
    
        self.toolbar = QToolBar("Log")
        self.log = QListWidget(self)
        self.toolbar.addWidget(self.log)
        self.addToolBar(self.toolbar)
        
        self.tabs=Tabs()
        win.setCentralWidget(self.tabs.tabFiles)
        self.api = Api()
        self.setMenu
        self.setWindowTitle("PyQt6 - Codeloop.org")
        self.setWindowIcon(QIcon("deluxeedit.png"))

