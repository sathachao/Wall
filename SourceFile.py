__author__ = 'Satha'

from PySide.QtGui import *


class SourceFile(QStandardItem):
    def __init__(self, filename, content):
        QStandardItem.__init__(self, filename)
        self.filename = filename
        self.content = content