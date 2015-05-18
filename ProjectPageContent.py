__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from PySide.QtCore import *
from ProjectCreateDialog import *
from WallObserver import *
from Member import *
from ProjectThumbnail import *
from Project import *
from CommentWidget import *
from TagEditWidget import *
from PhotoWidget import *
from Storage import *
from SourceFile import *


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
        self.sourcecodeTab.updateModel()
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

class ProjectDescriptionTab(QWidget, WallObserver):
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

    def updateObserver(self, user, history):
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

class ProjectCommentTab(QWidget, WallObserver):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        loader = QUiLoader()
        layout = QGridLayout(self)
        dialog = loader.load("./UI/projectComments.ui")
        self.commentArea = dialog.findChild(QScrollArea,"commentArea")
        self.sendBt = dialog.findChild(QPushButton,"sendBt")
        self.commentText = dialog.findChild(QTextEdit,"commentText")
        self.commentArea.setContentsMargins(0,0,0,0)
        widget = QWidget()
        self.commentLayout = QGridLayout(widget)
        self.commentArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
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
            for i in range (len(history[-1].comments)):
                self.commentLayout.addWidget(CommentWidget(history[-1].comments[i],self.system))
        else:
            self.hide()

class ProjectPhotoTab(QWidget,WallObserver):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        loader = QUiLoader()
        layout = QVBoxLayout(self)
        dialog = loader.load("./UI/projectPhotos.ui")
        self.addBt = dialog.findChild(QPushButton,"addBt")
        self.photoArea = dialog.findChild(QScrollArea,"photoArea")
        self.photoArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        widget = QWidget()
        self.photoLayout = QGridLayout(widget)
        self.photoLayout.setContentsMargins(0,0,0,0)
        self.photoArea.setWidget(widget)
        self.connect(self.addBt,SIGNAL("clicked()"),self.browsePhoto)

        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.hide()

    def browsePhoto(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file','./UI')
        self.system.addProjectPhoto(fname)

    def updateObserver(self,user,history):
        if type(history[-1]) == Project:
            if history[-1].owner.username != user.username:
                self.addBt.hide()
            else:
                self.addBt.show()
            while self.photoLayout.count()!= 0:
                widget = self.photoLayout.takeAt(0).widget()
                self.photoLayout.removeWidget(widget)
                widget.setParent(None)
            for i in range(len(history[-1].photos)):
                widget = PhotoWidget(self.system,history[-1].photos[i])
                self.photoLayout.addWidget(widget, i//3, i%3)

class ProjectSourcecodeTab(QWidget,WallObserver):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        loader = QUiLoader()
        layout = QVBoxLayout(self)
        dialog = loader.load("./UI/projectSourcecode.ui")
        self.addBt = dialog.findChild(QPushButton, "addBt")
        self.delBtt = dialog.findChild(QPushButton, "delBtt")
        self.sourcecodeTxt = dialog.findChild(QPlainTextEdit, "sourcecodeText")
        self.fileList = dialog.findChild(QListView, "fileList")

        self.model = QStandardItemModel(self)
        self.fileList.setModel(self.model)

        self.connect(self.addBt, SIGNAL("clicked()"), self.addFile)
        self.connect(self.delBtt, SIGNAL("clicked()"), self.delFile)
        self.connect(self.fileList.selectionModel(), SIGNAL("currentRowChanged(QModelIndex,QModelIndex)"),
            self.showSourceCode)

        self.updateModel()

        layout.addWidget(dialog)
        layout.setContentsMargins(0, 0, 0, 0)
        self.hide()

    def updateObserver(self,user,history):
        if type(history[-1]) == Project:
            if history[-1].owner.username != user.username:
                self.addBt.hide()
                self.delBtt.hide()

    def addFile(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFiles)
        dialog.setNameFilter("Python Files (*.py *.pyw)")

        if dialog.exec_():
            filenames = dialog.selectedFiles()
            for filename in filenames:
                file = open(filename, 'r')
                name = (filename.split("/"))[-1]
                content = file.read()
                Storage.saveSourceFile(self.system.history[-1].owner.username, self.system.history[-1].name,
                                       name, content)
            self.updateModel()

    def delFile(self):
        item = self.model.itemFromIndex(self.fileList.selectionModel().currentIndex())
        if item is not None:
            Storage.deleteSourceFile(self.system.user.username, self.system.history[-1].name, item.filename)
        self.updateModel()

    def updateModel(self):
        self.model.clear()
        if type(self.system.history[-1]) == Project:
            if self.system.history[-1].owner.username:
                files = Storage.loadSourceFiles(self.system.history[-1].owner.username, self.system.history[-1].name)
                for file in files:
                    self.model.appendRow(file)

    def showSourceCode(self, current, previous):
        if self.model.itemFromIndex(current) is not None:
            item = self.model.itemFromIndex(current)
            self.sourcecodeTxt.setPlainText(item.content)