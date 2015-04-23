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
        layout = QVBoxLayout()
        layout.addWidget(dialog)
        self.setLayout(layout)
        self.hide()

    def updateObserver(self,user,history):
        if type(history[-1]) == Wall:
            self.show()