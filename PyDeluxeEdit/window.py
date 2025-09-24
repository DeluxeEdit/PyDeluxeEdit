from os import path
from typing import Self
from PyQt6.QtWidgets import QTabWidget, QMainWindow,QMenuBar, QFileDialog, QStatusBar, QToolBar,QListWidget
from PyQt6.QtGui import QIcon, QAction
from models import TextTabItem, Tabs
from api import Api

class App(QMainWindow):
        
    def addAndLoadFile(filePath, hexView=False):
        tabName=path.basename(filePath)
        tab = TextTabItem()
        tab.filePath=filePath
        Self.tabFiles.addTab(tab, tabName)
        Self.tabsHelper.allTabs.append(tab)
        tab.text.append(Self.api.loadFile(filePath, hexView))
        formats= tab.text.document().allFormats()
        
        Self.status.showMessage("File:", filePath)

    def openFileDialog(hexView=False):
        dialog = QFileDialog(Self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Open File", "All files (*.*)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            if dialog.selectedFiles().length == 1:
                filePath = dialog.selectedFiles()[0]
                Self. addAndLoadFile(filePath, hexView)

    def saveAsDialog():
        filePath = QFileDialog.getSaveFileName(Self, "Save File", "All Files(*);;Text Files(*.txt)")
        if filePath:
            Self.api.saveFile(filePath,Self.tabsHelper.currentTab.text.document().toRawText())
            
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
        bar.show()
    def statusChanged(text):
        Self.log.addItem(text)

    def __init__(self):
        super().__init__()

        self.status = QStatusBar()

        self.status.messageChanged.connect(self.statusChanged)
        self.status.addPermanentWidget(self)
        self.toolbar = QToolBar("Log")
        self.log = QListWidget(self)
        self.toolbar.addWidget(self.log)
        self.addToolBar(self.toolbar)
        self.tabsHelper=Tabs()
        self.setCentralWidget(self.tabsHelper.tabFiles)
        self.api = Api()
        self.setMenu
        self.setWindowTitle("PyQt6 - Codeloop.org")
        self.setWindowIcon(QIcon("deluxeedit.png"))