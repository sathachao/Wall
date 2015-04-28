__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from PySide.QtCore import *
from Wall import *
from WallObserver import *
from Member import *

class TagEditWidget(QDialog,WallObserver):
    def __init__(self,system):
        QDialog.__init__(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.system = system
        self.system.addObserver(self)
        self.loader = QUiLoader()
        self.dialog = self.loader.load("./UI/tagEditDialog.ui")
        self.okBt = self.dialog.findChild(QPushButton,"okBt")
        self.removeBt = self.dialog.findChild(QPushButton,"removeBt")
        self.addBt = self.dialog.findChild(QPushButton,"addBt")
        self.cancelBt = self.dialog.findChild(QPushButton,"cancelBt")
        self.tagLine = self.dialog.findChild(QLineEdit,"tagLine")
        self.list = self.dialog.findChild(QListView,"list")
        layout = QVBoxLayout(self)
        layout.addWidget(self.dialog)
        self.cancelBt.clicked.connect(self.close)
        self.addBt.clicked.connect(self.add)
        self.removeBt.clicked.connect(self.remove)
        self.okBt.clicked.connect(self.confirm)
        self.model = QStandardItemModel(self.list)
        self.list.setModel(self.model)
        self.setModal(True)

    def confirm(self):
        tags = []
        for row in range(self.model.rowCount()):
            tags.append(self.model.item(row).text())
        if type(self.system.history[-1]) == Wall:
            self.system.editUserTags(tags)
        else:
            self.system.editProjectTags(self.system.history[-1],tags)
        self.close()

    def remove(self):
        self.model.takeRow(self.list.selectedIndexes()[0].row())

    def add(self):
        if self.tagLine.text() =="":
            return
        if len(self.model.findItems(self.tagLine.text()))==0:
            self.model.appendRow(QStandardItem(self.tagLine.text()))
            self.tagLine.setText("")

    def reject(self, *args, **kwargs):
        self.close()

    def closeEvent(self, *args, **kwargs):
        self.close()

    def updateObserver(self,user,history):
        if type(history[-1])==Member:
            tags =  history[-1].tags
        else:
            tags = history[-1].tags
        for tag in tags:
                self.model.appendRow((QStandardItem(tag)))


