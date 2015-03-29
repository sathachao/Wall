__author__ = 'Satha'

from PySide.QtCore import *
from PySide.QtGui import *

class ClickableLabel(QLabel):

    def __init__(self, qlabel):
        QLabel.__init__(self)


    def mouseReleaseEvent(self, event):
        self.emit(SIGNAL("clicked()"))