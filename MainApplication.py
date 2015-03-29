__author__ = 'Satha'

import sys
from PySide.QtCore import *
from PySide.QtGui import *

import LoginPage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginPage.LoginPage()
    window.show()
    sys.exit(app.exec_())