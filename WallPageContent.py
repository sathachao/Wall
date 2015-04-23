__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from PySide.QtCore import *
from ProjectCreateWidget import *
from WallObserver import *
from Wall import *
from Member import *

class WallPageContent(QWidget,WallObserver):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        loader = QUiLoader()
        layout = QVBoxLayout()
        dialog = loader.load("./UI/wallPageContent.ui")
        self.addBt = dialog.findChild(QPushButton,"addBt")
        self.connect(self.addBt,SIGNAL("clicked()"),self.addProject)
        layout.addWidget(dialog)
        self.setLayout(layout)
        self.hide()

    def addProject(self):
        self.dialog = ProjectCreateWidget(self.system)
        self.dialog.show()

    def updateObserver(self,user,history):
        if type(history[-1]) == Wall:
            self.show()