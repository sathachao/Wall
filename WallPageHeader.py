__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *


class WallPageHeader(QWidget):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        loader = QUiLoader()
        dialog = loader.load("./UI/wallPageHeader.ui")
        layout = QVBoxLayout()
        layout.addWidget(dialog)
        self.setLayout(layout)
