__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from WallObserver import *
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
        layout.addWidget(dialog)
        self.setLayout(layout)
        self.hide()

    def updateObserver(self,user,history):
        if type(history[-1]) == Wall:
            self.show()