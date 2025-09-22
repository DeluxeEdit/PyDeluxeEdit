from fileinput import filename
from os import path
from typing import Self
from PyQt6.QtWidgets import QWidget,QTabWidget, QTextEdit, QMainWindow, QFormLayout,QMenuBar, QFileDialog, QStatusBar, QToolBar,QListWidget
from PyQt6.QtGui import QIcon, QAction
from api import Api


class TextTabItem(QWidget):

    def onTextChanged(text):
        print("Text changed.>>> ")

    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        self.setLayout(layout)
        self.text = QTextEdit()
        layout.addRow(self.text)
        self.text.textChanged.connect(self.onTextChanged)


class App(QMainWindow):

    def loadAddFile(filePath, hexView=False):
        tabName=path.basename(filePath)
        tab = TextTabItem()
        Self.tabFiles.addTab(tab, tabName)
        tab.text = Self.api.loadFile(filePath, hexView)
        Self.status.showMessage("File:", filePath)

    def openFileDialog(hexView=False):
        dialog = QFileDialog(Self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Open File", "All files (*.*)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            if dialog.selectedFiles().length == 1:
                file = dialog.selectedFiles()[0]
                Self.loadAddFile(file, hexView)

    def saveAsDialog():
        file = QFileDialog.getSaveFileName(
            Self, "Save File", "All Files(*);;Text Files(*.txt)"
        )
        if file:

            def doHexView():
                Self.openFileDialog(True)

    def setMenu():
        bar = QMenuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        openMenu = QAction("Open")
        openMenu.setShortcut("Ctrl+O")
        hexViewMenu = QAction("Hex view")
        hexViewMenu.setShortcut("Ctrl+H")
        save = QAction("Save")
        save.setShortcut("Ctrl+S")
        file.addAction(save, Self.saveAsDialog)
        file.addAction(openMenu, Self.openFileDialog)
        file.addAction(hexViewMenu, Self.doHexView)

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
        self.addToolbar(self.toolbar)
        
        self.tabFiles = QTabWidget()
        self.setCentralWidget(self.tabFiles)
        self.api = Api()
        self.setMenu()
        self.setWindowTitle("PyQt6 - Codeloop.org")
        self.setWindowIcon(QIcon("deluxeedit.png"))