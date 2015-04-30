__author__ = 'Satha'

from PySide.QtGui import *
from PySide.QtCore import *
from Storage import *
from SearchBoxModel import *

class SearchBox(QComboBox):
    def __init__(self, parent=None):
        QComboBox.__init__(self, parent)
        self.model = SearchBoxModel()
        self.setModel(self.model)
        self.installEventFilter(self)

    def eventFilter(self, widget, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return:
                self.focusWidget()
                self.model.update(self.currentText())
                self.showPopup()

        return QComboBox.eventFilter(self, widget, event)

    def getItem(self):
        return self.model.item(self.currentIndex())
'''
    def eventFilter(self, widget, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return:
                self.showPopup()
            txt = self.currentText()
            self.clear()
            self.addItem(txt)
        if event.type() == QEvent.KeyRelease:
            txt = self.currentText()
            members = Storage.findUser(txt)
            memberList = list()
            if members is not None:
                #memberList.append(txt)
                for member in members:
                    memberList.append(member.firstname + " " + member.lastname)
                self.addItems(memberList)
            else:
                self.addItem(txt)


        return QComboBox.eventFilter(self, widget, event)
'''