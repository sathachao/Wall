__author__ = 'Satha'

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import *

class LoginPage(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("Wall Authentication System")

        loader = QUiLoader()
        self.ui = loader.load("./UI/loginPage.ui", self)
        print(self.ui)

        self.loginBtt = self.ui.findChild(QLabel, "loginBtt")


