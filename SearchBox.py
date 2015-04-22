__author__ = 'Satha'

from PySide.QtGui import *
from PySide.QtCore import *
from Storage import *

class SearchBox(QComboBox):
    def __init__(self, parent=None):
        QComboBox.__init__(self, parent)

    def editTextChanged(self, text):
        members = Storage.getUser(self.currentText())
        memberList = list()
        for member in members:
            memberList.append(member.firstname + " " + member.lastname)
        self.clear()
        self.addItems(memberList)
        self.showPopup()
