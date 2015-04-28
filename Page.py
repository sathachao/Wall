__author__ = 'Faaiz'
from PySide.QtGui import *
from PySide.QtUiTools import *
from WallPageContent import *
from WallPageHeader import *
from WallPageTab import *
from ProjectPageHeader import *
from ProjectPageTab import *
from ProjectPageContent import *
import UI.wallPageHeaderRsc_rc
from SearchBar import *

class Page():
    def __init__(self, sys):
        self.system = sys
        loader = QUiLoader()
        self.dialog = loader.load("./UI/page.ui", None)
        self.headerFrame = self.dialog.findChild(QFrame,"headerFrame")
        self.contentFrame = self.dialog.findChild(QFrame,"contentFrame")
        self.tabFrame = self.dialog.findChild(QFrame,"tabFrame")
        self.searchBarFrame = self.dialog.findChild(QFrame,"searchBarFrame")

        self.headerFrame.setContentsMargins(0,0,0,0)
        self.tabFrame.setContentsMargins(0,0,0,0)
        self.contentFrame.setContentsMargins(0,0,0,0)
        self.searchBarFrame.setContentsMargins(0,0,0,0)

        self.headerLayout = QVBoxLayout()
        self.headerLayout.setContentsMargins(0,0,0,0)
        self.tabLayout = QVBoxLayout()
        self.tabLayout.setContentsMargins(0,0,0,0)
        self.contentLayout = QVBoxLayout()
        self.contentLayout.setContentsMargins(0,0,0,0)
        self.searchBarLayout = QVBoxLayout()
        self.searchBarLayout.setContentsMargins(0,0,0,0)

        self.wallPageHeader = WallPageHeader(self.system)
        self.wallPageContent = WallPageContent(self.system)
        self.wallPageTab = WallPageTab(self.system)

        self.projectPageHeader = ProjectPageHeader(self.system)
        self.projectPageContent = ProjectPageContent(self.system)
        self.projectPageTab = ProjectPageTab(self.system,self.projectPageContent)

        self.headerLayout.addWidget(self.wallPageHeader)
        self.contentLayout.addWidget(self.wallPageContent)
        self.tabLayout.addWidget(self.wallPageTab)
        self.headerLayout.addWidget(self.projectPageHeader)
        self.tabLayout.addWidget(self.projectPageTab)
        self.contentLayout.addWidget(self.projectPageContent.descriptionTab)
        self.contentLayout.addWidget(self.projectPageContent.commentTab)
        self.contentLayout.addWidget(self.projectPageContent.photoTab)
        self.contentLayout.addWidget(self.projectPageContent.sourcecodeTab)
        self.searchBarLayout.addWidget(SearchBar(self.system))

        self.headerFrame.setLayout(self.headerLayout)
        self.tabFrame.setLayout(self.tabLayout)
        self.contentFrame.setLayout(self.contentLayout)
        self.searchBarFrame.setLayout(self.searchBarLayout)
        self.dialog.show()



