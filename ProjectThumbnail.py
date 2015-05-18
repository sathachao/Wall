__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from ClickableLabel import *
from WallObserver import*
from Member import *


class ProjectThumbnail(QWidget,WallObserver):
    def __init__(self,project,system):
        QWidget.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        self.project = project
        loader = QUiLoader()
        dialog = loader.load("./UI/projectThumbnail.ui")
        self.nameText = dialog.findChild(QLabel,"name")
        self.picture = dialog.findChild(ClickableLabel,"label")
        self.removeBt = dialog.findChild(QPushButton,"removeBt")

        self.nameText.setText(self.project.name)
        self.system.fitText(self.nameText,250,20)
        self.connect(self.removeBt,SIGNAL("clicked()"),self.remove)
        self.connect(self.picture,SIGNAL("clicked()"),self.openProject)
        layout = QVBoxLayout(self)
        layout.addWidget(dialog)

    def remove(self):
        self.system.removeProject(self.project)

    def openProject(self):
        self.system.openProject(self.project)

    def updateObserver(self,user,history):
        if type(history[-1])==Member:
            if history[-1].username == user.username:
                self.removeBt.show()
            else:
                self.removeBt.hide()