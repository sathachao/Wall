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
from CommentWidget import *
from TagEditWidget import *

class ProjectPageContent(WallObserver):
    def __init__(self,system):
        self.system = system
        self.system.addObserver(self)
        self.descriptionTab = ProjectDescriptionTab(self.system)
        self.commentTab = ProjectCommentTab(self.system)
        self.photoTab = ProjectPhotoTab(self.system)
        self.sourcecodeTab = ProjectSourcecodeTab(self.system)
        self.currentTab = self.descriptionTab

    def openDescriptionTab(self):
        self.currentTab.hide()
        self.currentTab = self.descriptionTab
        self.currentTab.show()

    def openCommentTab(self):
        self.currentTab.hide()
        self.currentTab = self.commentTab
        self.currentTab.show()

    def openSourcecodeTab(self):
        self.currentTab.hide()
        self.currentTab = self.sourcecodeTab
        self.currentTab.show()

    def openPhotoTab(self):
        self.currentTab.hide()
        self.currentTab = self.photoTab
        self.currentTab.show()

    def updateObserver(self,user,history):
        if type(self.system.history[-1])== Project:
            self.currentTab.show()
        else:
            self.currentTab.hide()
            self.currentTab = self.descriptionTab

class ProjectDescriptionTab(QWidget,WallObserver):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        loader = QUiLoader()
        layout = QVBoxLayout(self)
        dialog = loader.load("./UI/projectDescription.ui")
        self.descriptionText = dialog.findChild(QPlainTextEdit,"descriptionText")
        self.descriptionEditBt = dialog.findChild(QPushButton,"descriptionEditBt")
        self.saveBt = dialog.findChild(QPushButton,"saveBt")
        self.tagList = dialog.findChild(QListView,"tagList")
        self.tagEditBt = dialog.findChild(QPushButton,"tagEditBt")
        self.descriptionText.setReadOnly(True)
        self.model = QStandardItemModel(self.tagList)
        self.tagList.setModel(self.model)
        self.connect(self.tagEditBt,SIGNAL("clicked()"),self.editTag)
        self.connect(self.descriptionEditBt,SIGNAL("clicked()"),self.editDescription)
        self.connect(self.saveBt,SIGNAL("clicked()"),self.saveDescription)
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.hide()

    def editDescription(self):
        self.descriptionText.setReadOnly(False)

    def saveDescription(self):
        self.system.editProjectDescription(self.descriptionText.toPlainText())
        self.descriptionText.setReadOnly(True)

    def editTag(self):
        self.tagEdit = TagEditWidget(self.system)
        self.tagEdit.show()
        self.system.notifyObservers()

    def updateObserver(self,user,history):
        if type(history[-1]) == Project:
            if history[-1].owner.username != user.username:
                self.descriptionEditBt.hide()
                self.tagEditBt.hide()
            else:
                self.descriptionEditBt.show()
                self.tagEditBt.show()
            for tag in history[-1].tags:
                if len(self.model.findItems(tag))==0:
                    self.model.appendRow((QStandardItem(tag)))
            self.descriptionText.setPlainText(history[-1].description)

class ProjectCommentTab(QWidget,WallObserver):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        loader = QUiLoader()
        layout = QVBoxLayout(self)
        dialog = loader.load("./UI/projectComments.ui")
        self.commentArea = dialog.findChild(QScrollArea,"commentArea")
        self.sendBt = dialog.findChild(QPushButton,"sendBt")
        self.commentText = dialog.findChild(QTextEdit,"commentText")
        self.commentArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        widget = QWidget()
        widget.setContentsMargins(0,0,0,0)
        self.commentLayout = QVBoxLayout(widget)
        self.commentLayout.setContentsMargins(0,0,0,0)
        self.commentArea.setWidget(widget)
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)

        self.connect(self.sendBt,SIGNAL("clicked()"),self.send)

        self.hide()

    def send(self):
        self.system.addComment(self.commentText.toPlainText())
        self.commentText.clear()
        self.system.notifyObservers()

    def updateObserver(self,user,history):
        if type(history[-1])==Project:
            while self.commentLayout.count()!=0:
                widget = self.commentLayout.takeAt(0).widget()
                self.commentLayout.removeWidget(widget)
                widget.setParent(None)
            for comment in history[-1].comments:
                self.commentLayout.addWidget(CommentWidget(comment,self.system),Qt.AlignTop)
        else:
            self.hide()

class ProjectPhotoTab(QWidget):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        loader = QUiLoader()
        layout = QVBoxLayout(self)
        dialog = loader.load("./UI/projectPhotos.ui")
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.hide()


class ProjectSourcecodeTab(QWidget,WallObserver):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        loader = QUiLoader()
        layout = QVBoxLayout(self)
        dialog = loader.load("./UI/projectSourcecode.ui")
        self.addBt = dialog.findChild(QPushButton,"addBt")
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.hide()

    def updateObserver(self,user,history):
        if type(history[-1]) == Project:
            if history[-1].owner.username != user.username:
                self.addBt.hide()