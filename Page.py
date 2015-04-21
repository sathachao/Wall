__author__ = 'Faaiz'
from PySide.QtGui import *
from PySide.QtUiTools import *


class Page(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self,None)
        loader = QUiLoader()
        dialog = loader.load("./UI/page.ui", self)
        self.setCentralWidget(dialog)


