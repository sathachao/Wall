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
        self.picture = dialog.findChild(ClickableLabel,"label")
        self.connect(self.picture,SIGNAL("clicked()"),self.openProject)
        layout = QVBoxLayout()
        layout.addWidget(dialog)
        self.setLayout(layout)

    def openProject(self):
        self.system.history.append(self.project)
        self.system.notifyObservers()