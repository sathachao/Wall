__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from WallObserver import *
from Wall import *
from Project import *

class WallPageHeader(QWidget,WallObserver):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        loader = QUiLoader()
        dialog = loader.load("./UI/wallPageHeader.ui")
        self.nameText = dialog.findChild(QLabel,"name")
        layout = QVBoxLayout()
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        self.hide()

    def updateObserver(self,user,history):
        if type(history[-1]) == Wall:
            self.nameText.setText(history[-1].owner.firstname+" "+history[-1].owner.lastname)
            self.show()
        else:
            self.hide()