__author__ = 'Satha'

from PySide.QtGui import *
from PySide.QtCore import *

class SearchBox(QComboBox):
    def __init__(self, parent=None):
        QComboBox.__init__(self, parent)

    def textChanged(self, event):
        pass