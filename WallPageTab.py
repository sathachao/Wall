__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *


class WallPageTab(QWidget):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        loader = QUiLoader()
        layout = QVBoxLayout()
        dialog = loader.load("./UI/wallPageTab.ui")
        layout.addWidget(dialog)
        self.setLayout(layout)