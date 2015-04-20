__author__ = 'Satha'

from PySide.QtCore import *
from PySide.QtGui import *

class SearchTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        QTreeWidget.__init__(self, parent)