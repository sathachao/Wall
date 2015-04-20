__author__ = 'Satha'

from PySide.QtGui import *
from PySide.QtCore import *

class SearchBox(QLineEdit):
    def __init__(self, parent=None):
        QLineEdit.__init__(self, parent)

    def textChanged(self, event):
        pass