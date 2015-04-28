__author__ = 'Satha'

from PySide.QtGui import *
from Storage import *

class SearchBoxModel(QStandardItemModel):
    def __init__(self):
        QStandardItemModel.__init__(self)

    def update(self, txt):
        self.clear()
        members = Storage.findUser(txt)
        projects = Storage.findProject(txt)
        itemsWithTag = Storage.findItemsWithTag(txt)
        if members is not None:
            for member in members:
                self.appendRow(member)
        if projects is not None:
            for project in projects:
                self.appendRow(project)
        if itemsWithTag is not None:
            for itemWithTag in itemsWithTag:
                self.appendRow(itemWithTag)
