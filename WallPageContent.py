__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from PySide.QtCore import *
from ProjectCreateWidget import *

class WallPageContent(QWidget):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        loader = QUiLoader()
        layout = QVBoxLayout()
        dialog = loader.load("./UI/wallPageContent.ui")
        self.addBt = dialog.findChild(QPushButton,"addBt")
        self.connect(self.addBt,SIGNAL("clicked()"),self.addProject)
        layout.addWidget(dialog)
        self.setLayout(layout)

    def addProject(self):
        self.dialog = ProjectCreateWidget(self.system)
        self.dialog.show()