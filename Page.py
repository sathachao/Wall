__author__ = 'Faaiz'
from PySide.QtGui import *
from PySide.QtUiTools import *
from WallObserver import *
from WallPageContent import *
from WallPageHeader import *
from WallPageTab import *
from Member import *
from Project import *
import UI.wallPageHeaderRsc_rc


class Page():
    def __init__(self,sys):
        self.system = sys
        loader = QUiLoader()
        self.dialog = loader.load("./UI/page.ui", None)
        self.headerFrame = self.dialog.findChild(QFrame,"headerFrame")
        self.contentFrame = self.dialog.findChild(QFrame,"contentFrame")
        self.tabFrame = self.dialog.findChild(QFrame,"tabFrame")
        self.searchBarFrame = self.dialog.findChild(QFrame,"searchBarFrame")

        self.headerLayout = QVBoxLayout()
        self.tabLayout = QVBoxLayout()
        self.contentLayout = QVBoxLayout()

        self.wallPageHeader = WallPageHeader(self.system)
        self.wallPageContent = WallPageContent(self.system)
        self.wallPageTab = WallPageTab(self.system)

        self.headerLayout.addWidget(self.wallPageHeader)
        self.contentLayout.addWidget(self.wallPageContent)
        self.tabLayout.addWidget(self.wallPageTab)
        self.headerFrame.setLayout(self.headerLayout)
        self.tabFrame.setLayout(self.tabLayout)
        self.contentFrame.setLayout(self.contentLayout)
        self.dialog.show()



