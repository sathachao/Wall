__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from WallObserver import *
from PySide.QtCore import *
from ProjectCreateWidget import *
from Project import *
from Wall import *

class WallPageTab(QWidget,WallObserver):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        loader = QUiLoader()
        layout = QVBoxLayout()
        dialog = loader.load("./UI/wallPageTab.ui")
        self.editTagBt = dialog.findChild(QPushButton,"editTagBt")
        self.connect(self.editTagBt,SIGNAL("clicked()"),self.openProjectCreate)
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        self.hide()

    def openProjectCreate(self):
        self.projectCreteWidget = ProjectCreateWidget(self.system)
        self.projectCreteWidget.show()

    def updateObserver(self,user,history):
        if type(history[-1]) == Wall:
            self.show()
        else:
            self.hide()