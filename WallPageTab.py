__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from WallObserver import *
from PySide.QtCore import *
from ProjectCreateWidget import *
from Project import *
from TagEditWidget import *
from Member import *

class WallPageTab(QWidget,WallObserver):
    def __init__(self,system):
        QWidget.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        loader = QUiLoader()
        layout = QVBoxLayout(self)
        dialog = loader.load("./UI/wallPageTab.ui")
        self.editTagBt = dialog.findChild(QPushButton,"editTagBt")
        self.tagList = dialog.findChild(QListView,"tagList")
        self.model = QStandardItemModel(self.tagList)
        self.tagList.setModel(self.model)
        self.connect(self.editTagBt,SIGNAL("clicked()"),self.openTagEdit)
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.hide()

    def openTagEdit(self):
        self.tagEditWidget = TagEditWidget(self.system)
        self.tagEditWidget.show()
        self.system.notifyObservers()

    def updateObserver(self,user,history):
        if type(history[-1]) == Member:
            if history[-1].username != user.username:
                self.editTagBt.hide()
            else:
                self.editTagBt.show()
            self.model.clear()
            for tag in history[-1].tags:
                self.model.appendRow(QStandardItem(tag))
            self.show()
        else:
            self.hide()