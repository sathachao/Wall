__author__ = 'Satha'

from PySide.QtGui import *
from Storage import *

class SearchBoxModel(QStandardItemModel):
    def __init__(self):
        QStandardItemModel.__init__(self)

    def update(self, txt):
        self.clear()
        members = Storage.findUser(txt)
        if members is not None:
            for member in members:
                self.appendRow(member)
