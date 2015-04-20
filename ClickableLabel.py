__author__ = 'Satha'

from PySide.QtCore import *
from PySide.QtGui import *

class ClickableLabel(QLabel):
    def __init__(self,parent= None):
        QLabel.__init__(self, parent)

    def mouseReleaseEvent(self, e):
        QLabel.mouseReleaseEvent(self,e)
        self.emit(SIGNAL("clicked()"))


