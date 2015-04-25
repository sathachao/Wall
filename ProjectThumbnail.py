__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from ClickableLabel import *


class ProjectThumbnail(QWidget):
    def __init__(self,project,system):
        QWidget.__init__(self,None)
        self.system = system
        self.project = project
        loader = QUiLoader()
        dialog = loader.load("./UI/projectThumbnail.ui")
        self.nameText = dialog.findChild(QLabel,"name")
        self.picture = dialog.findChild(ClickableLabel,"label")
        self.removeBt = dialog.findChild(QPushButton,"removeBt")

        self.nameText.setText(self.project.name)
        self.connect(self.removeBt,SIGNAL("clicked()"),self.remove)
        self.connect(self.picture,SIGNAL("clicked()"),self.openProject)
        layout = QVBoxLayout()
        layout.addWidget(dialog)
        self.setLayout(layout)

    def remove(self):
        self.system.removeProject(self.project)
        self.system.notifyObservers()

    def openProject(self):
        self.system.history.append(self.project)
        self.system.notifyObservers()