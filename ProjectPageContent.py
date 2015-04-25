__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from PySide.QtCore import *
from ProjectCreateWidget import *
from WallObserver import *
from Wall import *
from Member import *
from ProjectThumbnail import *
from Project import *


class ProjectPageContent():
    def __init__(self,system):
        self.system = system
        self.descriptionTab = ProjectDescriptionTab(self.system)
        self.commentTab = ProjectCommentTab(self.system)
        self.photoTab = ProjectPhotoTab(self.system)
        self.sourcecodeTab = ProjectSourcecodeTab(self.system)
        self.currentTab = self.descriptionTab

    def openDescriptionTab(self):
        self.currentTab.hide()
        self.descriptionTab.show()
        self.currentTab = self.descriptionTab
    def openCommentTab(self):
        self.currentTab.hide()
        self.commentTab.show()
        self.currentTab = self.commentTab
    def openSourcecodeTab(self):
        self.currentTab.hide()
        self.sourcecodeTab.show()
        self.currentTab = self.sourcecodeTab
    def openPhotoTab(self):
        self.currentTab.hide()
        self.photoTab.show()
        self.currentTab = self.photoTab

class ProjectDescriptionTab(QWidget):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        loader = QUiLoader()
        layout = QVBoxLayout()
        dialog = loader.load("./UI/projectDescription.ui")
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        self.hide()


class ProjectCommentTab(QWidget):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        loader = QUiLoader()
        layout = QVBoxLayout()
        dialog = loader.load("./UI/projectComments.ui")
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        self.hide()


class ProjectPhotoTab(QWidget):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        loader = QUiLoader()
        layout = QVBoxLayout()
        dialog = loader.load("./UI/projectPhotos.ui")
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        self.hide()


class ProjectSourcecodeTab(QWidget):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        loader = QUiLoader()
        layout = QVBoxLayout()
        dialog = loader.load("./UI/projectSourcecode.ui")
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        self.hide()
