__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from WallObserver import *
from Project import *
from Member import *


class WallPageHeader(QWidget,WallObserver):
    def __init__(self, system):
        QWidget.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        loader = QUiLoader()
        dialog = loader.load("./UI/wallPageHeader.ui")
        self.nameText = dialog.findChild(QLabel,"name")
        layout = QVBoxLayout(self)
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.hide()

    def updateObserver(self,user,history):
        if type(history[-1]) == Member:
            self.nameText.setText(history[-1].firstname+" "+history[-1].lastname)
            self.system.fitText(self.nameText,430,40)
            self.show()
        else:
            self.hide()