__author__ = 'Faaiz'
from PySide.QtGui import *
from PySide.QtUiTools import *
from WallObserver import *
from WallPageContent import *
from WallPageHeader import *
from WallPageTab import *
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

        self.headerLayout = QVBoxLayout()
        self.tabLayout = QVBoxLayout()
        self.contentLayout = QVBoxLayout()

        self.wallPageHeader = WallPageHeader(self.system)
        self.wallPageContent = WallPageContent(self.system)
        self.wallPageTab = WallPageTab(self.system)

        self.currentHeader = self.wallPageHeader
        self.currentTab = self.wallPageTab
        self.currentContent = self.wallPageContent
        self.dialog.show()

    def updateObserver(self,user,directory,history):
        self.headerLayout.removeWidget(self.currentHeader)
        self.tabLayout.removeWidget(self.currentTab)
        self.contentLayout.removeWidget(self.currentContent)
        self.currentHeader.setParent(None)
        self.currentTab.setParent(None)
        self.currentContent.setParent(None)
        if directory=="WallPage":
            self.currentHeader = self.wallPageHeader
            self.currentTab = self.wallPageTab
            self.currentContent = self.wallPageContent
        self.headerLayout.addWidget(self.currentHeader)
        self.tabLayout.addWidget(self.currentTab)
        self.contentLayout.addWidget(self.currentContent)
        self.headerFrame.setLayout(self.headerLayout)
        self.tabFrame.setLayout(self.tabLayout)
        self.contentFrame.setLayout(self.contentLayout)






