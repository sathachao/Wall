__author__ = 'Faaiz'
from PySide.QtGui import *
from PySide.QtUiTools import *
from WallObserver import *
import UI.wallPageHeaderRsc_rc

class Page(WallObserver):
    def __init__(self,sys):
        self.system = sys
        self.system.addObserver(self)
        loader = QUiLoader()
        self.dialog = loader.load("./UI/page.ui", None)
        self.headerFrame = self.dialog.findChild(QFrame,"headerFrame")
        self.contentFrame = self.dialog.findChild(QFrame,"contentFrame")
        self.tabFrame = self.dialog.findChild(QFrame,"tabFrame")
        self.searchBarFrame = self.dialog.findChild(QFrame,"searchBarFrame")
        self.wallPageHeader = loader.load("./UI/wallPageHeader.ui")
        self.dialog.show()

    def updateObserver(self,user,directory,history):
        if directory=="WallPage":
            layout = QVBoxLayout()
            layout.addWidget(self.wallPageHeader)
            self.headerFrame.setLayout(layout)




