__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from PySide.QtCore import *
from ProjectCreateWidget import *
from WallObserver import *
from Member import *
from ProjectThumbnail import *


class WallPageContent(QWidget,WallObserver):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        loader = QUiLoader()
        layout = QVBoxLayout(self)
        dialog = loader.load("./UI/wallPageContent.ui")
        self.addBt = dialog.findChild(QPushButton,"addBt")
        self.thumbnailArea = dialog.findChild(QScrollArea,"thumbnailArea")
        self.thumbnailArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        widget = QWidget()
        self.thumbnailLayout = QGridLayout(widget)
        self.thumbnailArea.setWidget(widget)
        self.connect(self.addBt,SIGNAL("clicked()"),self.addProject)
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.hide()


    def addProject(self):
        self.dialog = ProjectCreateWidget(self.system)
        self.dialog.show()

    def updateObserver(self,user,history):
        if type(history[-1]) == Member:
            if history[-1].username != user.username:
                self.addBt.hide()
            else:
                self.addBt.show()
            while self.thumbnailLayout.count()!= 0:
                widget = self.thumbnailLayout.takeAt(0).widget()
                self.thumbnailLayout.removeWidget(widget)
                widget.setParent(None)
            for project in history[-1].projects:
                self.thumbnailLayout.addWidget(ProjectThumbnail(project,self.system))
            self.show()
        else:
            self.hide()